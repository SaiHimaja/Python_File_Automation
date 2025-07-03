import os

def extract_error(log_file_path, output_file_path):
    with open(log_file_path, 'r') as log_file:
        lines = log_file.readlines()

    err_lines = [line for line in lines if "error" in line.lower()]

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(err_lines)

def find_txt_files_and_extract_errors(start_dir, result_dir):
    os.makedirs(result_dir, exist_ok=True)

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.txt'):
                log_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(log_file_path, start_dir)
                output_file_path = os.path.join(result_dir, relative_path)

                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                extract_error(log_file_path, output_file_path)
                print(f"Extracted errors from {log_file_path} to {output_file_path}")

if __name__ == "__main__":
    start_directory = "./logs"        # Replace with your actual logs root directory
    output_directory = "./errors"     # Output directory to store error files
    find_txt_files_and_extract_errors(start_directory, output_directory)
