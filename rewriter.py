# rewriter.py – Memory Compression System

class MemoryRewriter:
    def __init__(self):
        pass

    def compress(self, memory):
        # Compress memory dict using basic rule
        return {k: v for k, v in memory.items() if len(v) < 1000}
