FROM scratch
COPY hello.wasm /hello.wasm
ENTRYPOINT [ "/hello.wasm" ]
