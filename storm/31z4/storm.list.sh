echo '----- storm list -----'
docker run -it --rm \
--name list \
--net container:nimbus \
31z4/storm:1.0.2 \
storm list
