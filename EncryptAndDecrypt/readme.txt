1.
#crontab -e

2. crontab 마지막 줄에 다음과 같이 추가
  0 14 * * * /backup/backupscript.sh
  10 14 * * * /backup/pythonscript.sh

  -> 매일 오후 2시 / 2시 10분에 위의 명령을 실행

3. 작업 목록 확인
#crontab -l 

