import os

# 변경할 디렉토리 경로 (원시 문자열 사용)
directory = r"C:\Users\hjcho\venture"

def replace_spaces_with_underscore_in_subdirectories(directory):
    # 먼저 하위 디렉토리 이름을 변경
    for root, dirs, files in os.walk(directory):
        # 현재 디렉토리에서 하위 디렉토리 이름 변경
        for dir_name in dirs:
            new_dir_name = dir_name.replace(" ", "_")  # 공백을 _로 변경
            if new_dir_name != dir_name:  # 이름이 변경된 경우에만
                try:
                    os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))
                    print(f"Renamed directory: {dir_name} to {new_dir_name}")  # 변경된 디렉토리 출력
                except PermissionError as e:
                    print(f"PermissionError: {e} for directory: {dir_name}")

    # 다음으로 파일 이름 변경 (하위 폴더 안의 파일 포함)
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            new_file_name = file_name.replace(" ", "_")  # 공백을 _로 변경
            if new_file_name != file_name:  # 이름이 변경된 경우에만
                try:
                    os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))
                    print(f"Renamed file: {file_name} to {new_file_name}")  # 변경된 파일 출력
                except PermissionError as e:
                    print(f"PermissionError: {e} for file: {file_name}")

replace_spaces_with_underscore_in_subdirectories(directory)
