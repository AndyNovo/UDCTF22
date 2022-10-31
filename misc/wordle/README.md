docker build -t wordle .
docker tag wordle registry.ctfd.io/bluehens/wordle
docker push registry.ctfd.io/bluehens/wordle
