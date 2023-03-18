image_name="check_connect_image"
container_name="check_connect_container"
# rm -f ./find_doctor/common.py
# cp ../common/common.py ./find_doctor/common.py
# cp ../private/tele.kdbx /home/tele_tok/tele.kdbx
docker stop ${container_name} && docker rm ${container_name}
docker build --rm -t ${image_name} --no-cache ./check_connect
# неочевидная хня с entrypoint https://oprearocks.medium.com/how-to-properly-override-the-entrypoint-using-docker-run-2e081e5feb9d
docker run \
--detach \
--name ${container_name} \
--env-file ./check_connect/env.env \
--restart=always \
-v /home/tele_tok/:/usr/src/app/token/ \
-v $(pwd)/check_connect/:/usr/src/app/ \
--entrypoint python3 ${image_name} ./check_provider.py
