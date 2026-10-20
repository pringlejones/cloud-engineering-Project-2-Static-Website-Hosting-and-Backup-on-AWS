import os
import boto3
from botocore.exceptions import NoCredentialsError

def upload_folder_to_s3(local_folder, bucket_name):
    # Initializes the secure S3 service client
    s3_client = boto3.client('s3')
    
    print(f"🚀 Starting deployment of '{local_folder}' to S3 bucket '{bucket_name}'...")
    
    # Walk through all directories and files in your local folder
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            
            # Create a clean relative path structural key for S3 compatibility
            relative_path = os.path.relpath(local_path, local_folder)
            s3_key = relative_path.replace("\\", "/") # Ensures Linux/Windows cross-compatibility
            
            try:
                # Upload file with public read access so the site updates live
                s3_client.upload_file(
                    local_path, 
                    bucket_name, 
                    s3_key,
                    ExtraArgs={'ContentType': 'text/html'} # Helps browsers render it instantly
                )
                print(f"✅ Successfully synced: {s3_key}")
            except FileNotFoundError:
                print(f"❌ Local file not found: {local_path}")
            except NoCredentialsError:
                print("❌ AWS Credentials missing. Run 'aws configure' in your terminal.")
                return

if __name__ == "__main__":
    # Change these values to match your local setup when running locally
    TARGET_LOCAL_FOLDER = "./website-assets"
    TARGET_S3_BUCKET = "YOUR-UNIQUE-BUCKET-NAME"
    
    upload_folder_to_s3(TARGET_LOCAL_FOLDER, TARGET_S3_BUCKET)
