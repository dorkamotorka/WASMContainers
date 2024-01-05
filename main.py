import docker
import logging as log
import time

log.basicConfig(
    level=log.INFO, filename="/dev/stdout",
    format="%(levelname)s: %(message)s"
)
cli = docker.from_env()

# C container
start = time.time()
container = cli.containers.run("dorkamotorka/hello-world-c", detach=True)
end = time.time()
log.info("Time took to execute the C container: %s seconds." % (end - start))
container.remove()

# WASM container
start = time.time()
container = cli.containers.run("dorkamotorka/hello-world-wasm", runtime="io.containerd.wasmedge.v1", platform="wasi/wasm", detach=True)
end = time.time()
log.info("Time took to execute the WASM container: %s seconds." % (end - start))
container.remove()

# WASM AOT container
start = time.time()
container = cli.containers.run("dorkamotorka/hello-world-wasm-aot", runtime="io.containerd.wasmedge.v1", platform="wasi/wasm", detach=True)
end = time.time()
log.info("Time took to execute the WASM AOT container: %s seconds." % (end - start))
container.remove()