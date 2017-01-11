# VOLUME /home/rstudio 
docker run -d \
    -p 8787:8787 \
    --volume=$HOME/rstudio:/home/rstudio \
    --name grss mobivi/rstudioserver
# username: rstudio
# password: rstudio
