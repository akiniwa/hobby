echo '----- storm jar -----'
docker run -it --rm \
--name submit \
--net container:nimbus \
-v /c/Users/realtime-tick-1.0-SNAPSHOT.jar:/topology.jar \
31z4/storm:1.0.2 \
storm jar /topology.jar com.jd.o2o.realtime.tick.topology.TickTopology
