# Running WASM on K8s (WIP)

"Wanna be" running WASM on K8s - but probably first try it on Docker Desktop (still in Beta ATM)

## Prerequisites

Follow `emscripten` install instruction [here](https://emscripten.org/docs/getting_started/downloads.html).

## Native

Compile your C code and run it using:
```
gcc hello.c -o hello.out
./hello.out
```

## Wasm

NOTE: `./emcc` script can be found in `emsdk/emscripten` directory.
```
`./emcc hello.c -o hello.wasm
```

Then you can run WASM script using WasmEdge runtime:
```
wasmedge hello.wasm
```

## In Docker

First create a `Dockerfile`, build it and push it using the following commands:
```
docker buildx build --platform wasi/wasm -t <username>/hello-world-wasm .
docker push <username>/hello-world-wasm
``` 

Then simply run the following command:
```
docker run \
  --runtime=io.containerd.wasmedge.v1 \
  --platform=wasi/wasm \
  <username>/hello-world-wasm
```
