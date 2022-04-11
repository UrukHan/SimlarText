docker build -t simlar .
docker run --rm --name rubert -p 8000:8000 simlar
docker run -d --name rubert -p 8000:8000 simlar

docker run --rm --gpus 'device=0' --name rusimlar -p 8000:8000 simlar
docker run -it -d --gpus 'device=0' --name rusimlar -p 8000:8000 simlar

/health_check
curl -X GET http://10.9.1.156:8000/api/health_check
curl -X POST -H "Content-Type: application/json" -d "{ \"textA\": \"Введите текст\", \"textB\": \"Введите текст\" }" http://testtextcategory-ai-cyrm.fdi.group/api/predict
curl -X POST -H "Content-Type: application/json" -d "{ \"textA\": \"Введите текст\", \"textB\": \"Введите текст\" }" http://172.20.192.1:8000/api/predict

curl -X POST -H "Content-Type: application/json" -d "{\"textA\": \"Введите текст\", \"textB\": \"Введите текст\" }" http://testtextcategory-ai-cyrm.fdi.group/api/predict


docker exec -it <container_id> bash
tensorflow==2.8.0

//RUN apt-get install nvidia-container-runtime



curl -X POST -H "Content-Type: application/json" -d "{ \"Лавров обвинил США в принуждении Зеленского к боевым действиям\": \"Введите текст\", \"Министр иностранных дел России Сергей Лавров обвинил США в попытке сформировать однополярный мир, в котором повестку определяет сильнейший, то есть Вашингтон\" }" 172.18.16.1:8000/api/predict


docker tag spell docker-ici-cyrm.fdi.group:443/spell:020422 

docker kill $(docker ps -a -q) 
docker rm $(docker ps -a -q)  
docker rmi $(docker images -a -q)

sudo chmod 666 /var/run/docker.sock

docker login http://docker-ici-cyrm.fdi.group:443
ici
cyrmE3r1x5a1J

docker tag news docker-ici-cyrm.fdi.group:443/class_news:310322
docker push docker-ici-cyrm.fdi.group:443/class_news:310322

docker tag t5 uruk/summarizet5:t5
<2sec cpu
curl -X POST -H "Content-Type: application/json" -d "{ \"input\": {\"texts\": [\"Лавров обвинил США в принуждении Зеленского к боевым действиям\", \"Власти США принуждают президента Украины Владимира Зеленского продолжать боевые действия и препятствуют достижению мира. Об этом рассказал министр иностранных дел РФ Сергей Лавров в видеокомментарии, который находится в распоряжении «Ленты.ру».\", \"Лавров обвинил США в принуждении Зеленского к боевым действиям\", \"Власти США принуждают президента Украины Владимира Зеленского продолжать боевые действия и препятствуют достижению мира. Об этом рассказал министр иностранных дел РФ Сергей Лавров в видеокомментарии, который находится в распоряжении «Ленты.ру».\", \"Лавров обвинил США в принуждении Зеленского к боевым действиям\", \"Власти США принуждают президента Украины Владимира Зеленского продолжать боевые действия и препятствуют достижению мира. Об этом рассказал министр иностранных дел РФ Сергей Лавров в видеокомментарии, который находится в распоряжении «Ленты.ру».\"]} }" 172.18.16.1:8000/api/predict