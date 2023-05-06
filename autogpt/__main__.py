"""Auto-GPT: A GPT powered AI Assistant"""
import autogpt.cli
import tracemalloc

if __name__ == "__main__":
    tracemalloc.start()
    autogpt.cli.main()
