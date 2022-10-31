docker build -t wordle-hard .
docker tag wordle registry.ctfd.io/bluehens/wordle-hard
docker push registry.ctfd.io/bluehens/wordle-hard
