# Running WASM on K8s (WIP)

"Wanna be" running WASM on K8s - but probably first try it on Docker Desktop (still in Beta ATM)

## Prerequisites

Follow `emscripten` install instruction [here](https://emscripten.org/docs/getting_started/downloads.html).

To be able to run it using Docker, please follow the instructions [here](https://docs.docker.com/desktop/wasm/).

## Deployments

### Native

Compile your C code and run it using:
```
gcc hello.c -o hello.out
./hello.out
```

### Wasm

NOTE: `./emcc` script can be found in `emsdk/emscripten` directory.
```
./emcc hello.c -o hello.wasm
```

Then you can run WASM script using WasmEdge runtime:
```
wasmedge --enable-all-statistics hello.wasm
```

### In Docker

First build the `Dockerfile` and push the images using the following commands:
```
docker build -t <username>/hello-world-c -f Dockerfile .
docker push <username>/hello-world-c

# WASM in Container
docker buildx build --platform wasi/wasm -t <username>/hello-world-wasm .
docker push <username>/hello-world-wasm
``` 

Then simply run the following command:
```
docker run <username>/hello-world-c

# Just for testing - not used for benchmarking
docker run \
  --runtime=io.containerd.wasmedge.v1 \
  --platform=wasi/wasm \
  <username>/hello-world-wasm
```
