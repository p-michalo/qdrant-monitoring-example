import sys
from qdrant_client import QdrantClient
if len(sys.argv) > 1:
    snapshotURL = sys.argv[1]
else:
    print("Snapshot URL not given, taking default...")
    snapshotURL = "https://snapshots.qdrant.io/wolt-clip-ViT-B-32-2446808438011867-2023-12-14-15-55-26.snapshot"

client = QdrantClient("localhost", port=6333)

print("!!!!!!!!! Starting recovery with -> " + snapshotURL)
client.recover_snapshot(
    "test",
    snapshotURL,
)