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
container = cli.containers.run("dorkamotorka/hello-world-c", ["/app/hello.out"])
end = time.time()
log.info("Time took to execute the container: %s seconds." % (end - start))
