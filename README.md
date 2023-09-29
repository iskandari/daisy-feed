# daisy-feed

**MacOS**

Build
```bash
brew install websocat
docker build -t daisy-feed .
```

Run

```bash
docker run -p 8080:5000 -e SERIAL_PORT=/dev/ttyUSB0 daisy-feed
```
For [Norwegian livestream](https://pyais.readthedocs.io/en/latest/examples.html)
change command to `norge_ais:app`


Listen
```bash
websocat ws://localhost:8080/ws  

{"mmsi":257103840,"speed":0.0,"lat":65.469302,"lon":12.199682,"course":228.0,"heading":511}
{"mmsi":258043000,"speed":5.7,"lat":66.74328,"lon":13.197147,"course":217.5,"heading":221,"status":0,"turn":0.0}
```



### Requirements

- Docker
- dAISY plugged in
- [websocat](https://github.com/vi/websocat)