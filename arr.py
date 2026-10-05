def main():
    scores = [78,85,90,66,88]
    total = sum(scores)
    average = total/len(scores)
    print("=== main/master branch output ===")
    print(f"Scores:{scores}")
    print(f"Sum:{total}")
    print(f"Average:{average}")
if __name__ == "__main__":
    main()