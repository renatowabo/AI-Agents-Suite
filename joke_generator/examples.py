"""
Joke Generator Examples - Various usage patterns
"""

from joke_generator import JokeGenerator

def example_1_random_joke():
    """Example 1: Get a random joke."""
    print("\n" + "="*70)
    print("Example 1: Get a Random Joke")
    print("="*70)
    
    generator = JokeGenerator()
    joke = generator.get_random_joke()
    generator.print_joke(joke)

def example_2_programming_jokes():
    """Example 2: Get programming jokes."""
    print("\n" + "="*70)
    print("Example 2: Get Programming Jokes")
    print("="*70)
    
    generator = JokeGenerator()
    
    for i in range(3):
        print(f"\n--- Programming Joke {i+1} ---")
        joke = generator.get_programming_joke()
        generator.print_joke(joke)

def example_3_safe_jokes():
    """Example 3: Get family-friendly jokes."""
    print("\n" + "="*70)
    print("Example 3: Get Safe (Family-Friendly) Jokes")
    print("="*70)
    
    generator = JokeGenerator()
    
    for i in range(3):
        print(f"\n--- Safe Joke {i+1} ---")
        joke = generator.get_safe_joke()
        generator.print_joke(joke)

def example_4_different_categories():
    """Example 4: Get jokes from different categories."""
    print("\n" + "="*70)
    print("Example 4: Jokes from Different Categories")
    print("="*70)
    
    generator = JokeGenerator()
    categories = ['General', 'Programming', 'Knock-Knock', 'Pun']
    
    for category in categories:
        print(f"\n--- {category} Joke ---")
        joke = generator.search_jokes_by_category(category)
        generator.print_joke(joke)

def example_5_batch_jokes():
    """Example 5: Get multiple jokes in batch."""
    print("\n" + "="*70)
    print("Example 5: Batch Retrieval - Get 5 Random Jokes")
    print("="*70)
    
    generator = JokeGenerator()
    jokes = generator.get_jokes_batch(count=5)
    
    for i, joke in enumerate(jokes, 1):
        print(f"\n--- Joke {i}/5 ---")
        generator.print_joke(joke)

def example_6_joke_comparison():
    """Example 6: Compare jokes from different sources."""
    print("\n" + "="*70)
    print("Example 6: Compare Jokes from Different Sources")
    print("="*70)
    
    generator = JokeGenerator()
    
    print("\n--- Joke from JokeAPI ---")
    joke1 = generator.get_joke_from_jokeapi(category='Programming')
    generator.print_joke(joke1)
    
    print("\n--- Joke from Official Joke API ---")
    joke2 = generator.get_joke_from_official_api()
    generator.print_joke(joke2)

def example_7_error_handling():
    """Example 7: Handle errors gracefully."""
    print("\n" + "="*70)
    print("Example 7: Error Handling")
    print("="*70)
    
    generator = JokeGenerator()
    
    # Try to get joke with invalid category
    print("\n--- Attempting Invalid Category ---")
    joke = generator.search_jokes_by_category('InvalidCategory')
    
    if 'error' in joke:
        print(f"❌ {joke['error']}")
    else:
        generator.print_joke(joke)
    
    # Get joke successfully
    print("\n--- Getting Valid Joke ---")
    joke = generator.get_random_joke()
    generator.print_joke(joke)

def example_8_custom_filtering():
    """Example 8: Custom filtering with different types."""
    print("\n" + "="*70)
    print("Example 8: Custom Filtering - Different Joke Types")
    print("="*70)
    
    generator = JokeGenerator()
    
    print("\n--- Single-Line Joke ---")
    single = generator.get_joke_from_jokeapi(joke_type='single')
    generator.print_joke(single)
    
    print("\n--- Two-Part Joke ---")
    twopart = generator.get_joke_from_jokeapi(joke_type='twopart')
    generator.print_joke(twopart)

def example_9_statistics():
    """Example 9: View API statistics and information."""
    print("\n" + "="*70)
    print("Example 9: API Statistics and Information")
    print("="*70)
    
    generator = JokeGenerator()
    stats = generator.get_statistics()
    
    print(f"\n🔗 Available Sources:")
    for source in stats['available_sources']:
        print(f"   • {source}")
    
    print(f"\n📂 Available Categories:")
    for cat in stats['jokeapi_categories']:
        print(f"   • {cat}")
    
    print(f"\n📝 Joke Types:")
    for jtype in stats['jokeapi_types']:
        print(f"   • {jtype}")
    
    print(f"\n✨ Features:")
    for feature in stats['features']:
        print(f"   • {feature}")
    
    print(f"\n📚 Category Descriptions:")
    for cat, desc in stats['example_categories'].items():
        print(f"   • {cat}: {desc}")

def example_10_custom_response_handling():
    """Example 10: Custom handling of joke responses."""
    print("\n" + "="*70)
    print("Example 10: Custom Response Handling")
    print("="*70)
    
    generator = JokeGenerator()
    joke = generator.get_programming_joke()
    
    if 'error' not in joke:
        print(f"\nJoke Type: {joke.get('type', 'unknown')}")
        print(f"Category: {joke.get('category', 'unknown')}")
        
        if joke.get('joke'):
            print(f"\nJoke: {joke['joke']}")
        elif joke.get('setup'):
            print(f"\nSetup: {joke['setup']}")
            if 'delivery' in joke:
                print(f"Delivery: {joke['delivery']}")
            elif 'punchline' in joke:
                print(f"Punchline: {joke['punchline']}")
        
        # Check for content warnings
        if any([joke.get('nsfw'), joke.get('religious'), 
                joke.get('political'), joke.get('racist'), 
                joke.get('sexist')]):
            print("\n⚠️  Content Warnings:")
            if joke.get('nsfw'):
                print("   • NSFW content")
            if joke.get('religious'):
                print("   • Religious references")
            if joke.get('political'):
                print("   • Political content")
            if joke.get('racist'):
                print("   • Potentially racist content")
            if joke.get('sexist'):
                print("   • Potentially sexist content")

def main():
    """Run all examples."""
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#" + "  RANDOM JOKE GENERATOR - EXAMPLES".center(68) + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    examples = [
        ("1", "Random Joke", example_1_random_joke),
        ("2", "Programming Jokes", example_2_programming_jokes),
        ("3", "Safe (Family-Friendly) Jokes", example_3_safe_jokes),
        ("4", "Different Categories", example_4_different_categories),
        ("5", "Batch Retrieval", example_5_batch_jokes),
        ("6", "Compare Sources", example_6_joke_comparison),
        ("7", "Error Handling", example_7_error_handling),
        ("8", "Custom Filtering", example_8_custom_filtering),
        ("9", "Statistics", example_9_statistics),
        ("10", "Custom Response Handling", example_10_custom_response_handling),
    ]
    
    print("\nAvailable Examples:")
    for num, title, _ in examples:
        print(f"  {num}. {title}")
    
    while True:
        try:
            choice = input("\nSelect an example (1-10) or 'all' or 'quit': ").strip().lower()
            
            if choice == 'quit':
                print("\n👋 Thanks for checking out the examples! 😂\n")
                break
            elif choice == 'all':
                for _, _, func in examples:
                    func()
                print("\n" + "#"*70)
                print("#" + " All examples completed!".center(68) + "#")
                print("#"*70 + "\n")
                break
            elif choice.isdigit() and 1 <= int(choice) <= 10:
                func = examples[int(choice)-1][2]
                func()
            else:
                print("❌ Invalid input. Please select 1-10, 'all', or 'quit'.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! 😄\n")
            break

if __name__ == "__main__":
    main()
