# Powershell_wsl 執行tasks指令:
- ansible-playbook -i hosts ecx01_install.yml
- ansible-playbook -i hosts ecx01_install.yml --check --diff --step
- ansible-playbook -i hosts docker_test.yml --step

# Docker 是一種開源的容器化平台，能將應用程式及其所有依賴環境打包成一個標準化的執行單元（容器），確保程式在任何電腦上都能以相同的方式順利運行。
docker build -t {名稱 .} Build 會在docker建立images
docker build -t ft001-ansible .
docker start -a demo

測試流程
1.VS確認hosts_SSH設定
2.要在終端build => docker build -t 檔名 .
3.GUI docker => 到 Images Run 檔名
4.docker Containers => Logs紀錄

docker啟動卡住重啟	Get-Process *docker* 
 - ErrorAction SilentlyContinue | Stop-Process -Force			
 - Get-Process *docker* -ErrorAction SilentlyContinue

打包清單	
- docker buildx history ls

刪除打包資料	
- docker buildx history rm <完整的 h3iviq... BUILD ID>			