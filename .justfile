explore:
    podman run -p 8000:8000 \
           -v ./data/internal/kuzu-db:/database:U \
           --rm kuzudb/explorer:latest

