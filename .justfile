explore:
    podman run -p 8000:8000 \
           -v ./data/kumls:/database:U \
           --rm kuzudb/explorer:latest

