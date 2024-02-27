# 자동으로 .git 폴더 삭제 해주는 코드.
# 현재 폴더를 기준으로 모든 폴더를 조사하여서,
# .git 폴더를 삭제 한다.
    # 단, 최상위 폴더 (코드가 실행된 위치의 .git은 제외하고)
# os 파이썬 표준 라이브러리 -> 운영 체제와 상호 작용 가능
import os
import subprocess

# get current working directory
# print(os.getcwd())
# os.chdir('01_python/')
# print(os.getcwd())
# os.removedirs

# 현재 폴더 경로를 변수에 저장
current_folder = os.getcwd()
# 현재 폴더 및 모든 하위 폴더를 반복
for foldername, subfolders, filenames in os.walk(current_folder):
    # print(foldername, 'fn')
    # print(subfolders, 'sf')
    # print(filenames, 'fn')
    # 하위 폴더 목록에 .git이 있다면
    if '.git' in subfolders:
        # root 디렉토리는 제외
        if foldername == current_folder:
            continue    # 반복문의 continue -> 아래코드 실행하지말고 다음 순회
        # 그 외 모든 경우에 대해서
        # .git 폴더를 삭제 하도록 할 것이다.
        # 삭제하려는 .git 폴더의 위치를 변수에 저장
        # print(os.path)
        git_folder_path = os.path.join(foldername, '.git')
        # 경로 : '' + '' X
        # 경로 : 'folder' + '.git' -> folder/.git 
        # os.rmdir(git_folder_path)
        # break
        # rm -rf 폴더 경로
        subprocess.run(['rm', '-rf', git_folder_path])
        print(f'{git_folder_path} 폴더가 삭제되었습니다.')