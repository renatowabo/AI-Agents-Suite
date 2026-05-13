"""
Random Joke Generator - Fetch jokes from external APIs
Supports multiple joke sources and formats
"""

import requests
import json
from typing import Optional, Dict, List
from enum import Enum
import random

class JokeCategory(Enum):
    """Joke categories supported by JokeAPI."""
    GENERAL = "General"
    PROGRAMMING = "Programming"
    KNOCK_KNOCK = "Knock-Knock"
    DARK = "Dark"
    SPOOKY = "Spooky"
    PUN = "Pun"

class JokeType(Enum):
    """Joke formats."""
    SINGLE = "single"  # Single line joke
    TWO_PART = "twopart"  # Setup and delivery
    ANY = "any"

class JokeGenerator:
    """Generate random jokes from external APIs."""
    
    def __init__(self):
        """Initialize the Joke Generator."""
        self.jokeapi_url = "https://v2.jokeapi.dev/joke"
        self.official_joke_api_url = "https://official-joke-api.appspot.com"
        self.useless_facts_api = "https://uselessfacts.jscinema.com/random.json"
        self.headers = {
            'User-Agent': 'JokeGenerator/1.0'
        }
    
    def get_joke_from_jokeapi(self, 
                              category: str = "Any",
                              joke_type: str = "any",
                              safe_mode: bool = False) -> Dict:
        """
        Fetch a joke from JokeAPI.
        
        Args:
            category: Joke category (Any, General, Programming, Knock-Knock, Dark, Spooky, Pun)
            joke_type: Format (single, twopart, any)
            safe_mode: Filter out explicit jokes if True
            
        Returns:
            Dictionary containing joke data
        """
        try:
            # Build the endpoint
            endpoint = f"{self.jokeapi_url}/{category}"
            
            # Add parameters
            params = {
                'type': joke_type,
                'format': 'json'
            }
            
            if safe_mode:
                params['safe-mode'] = 'true'
            
            response = requests.get(endpoint, params=params, headers=self.headers, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('error'):
                return {'error': 'No jokes found for this category/type'}
            
            return {
                'source': 'JokeAPI',
                'category': data.get('category', 'General'),
                'type': data.get('type', 'single'),
                'joke': data.get('joke'),
                'setup': data.get('setup'),
                'delivery': data.get('delivery'),
                'nsfw': data.get('flags', {}).get('nsfw', False),
                'religious': data.get('flags', {}).get('religious', False),
                'political': data.get('flags', {}).get('political', False),
                'racist': data.get('flags', {}).get('racist', False),
                'sexist': data.get('flags', {}).get('sexist', False)
            }
            
        except requests.exceptions.RequestException as e:
            return {'error': f'Failed to fetch joke from JokeAPI: {str(e)}'}
    
    def get_joke_from_official_api(self, joke_type: str = 'random') -> Dict:
        """
        Fetch a joke from Official Joke API.
        
        Args:
            joke_type: 'random' for random joke, or specific ID
            
        Returns:
            Dictionary containing joke data
        """
        try:
            if joke_type == 'random':
                endpoint = f"{self.official_joke_api_url}/random_joke"
            else:
                endpoint = f"{self.official_joke_api_url}/jokes/{joke_type}/random"
            
            response = requests.get(endpoint, headers=self.headers, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if isinstance(data, list) and len(data) > 0:
                data = data[0]
            
            return {
                'source': 'Official Joke API',
                'type': data.get('type', 'general'),
                'setup': data.get('setup'),
                'punchline': data.get('punchline'),
                'id': data.get('id'),
                'joke_id': data.get('joke_id'),
                'full_joke': f"{data.get('setup', '')} {data.get('punchline', '')}".strip()
            }
            
        except requests.exceptions.RequestException as e:
            return {'error': f'Failed to fetch joke from Official Joke API: {str(e)}'}
    
    def get_programming_joke(self) -> Dict:
        """
        Get a programming-specific joke.
        
        Returns:
            Dictionary containing programming joke
        """
        return self.get_joke_from_jokeapi(category='Programming', joke_type='any')
    
    def get_dark_joke(self) -> Dict:
        """
        Get a dark/edgy joke.
        
        Returns:
            Dictionary containing dark joke
        """
        return self.get_joke_from_jokeapi(category='Dark', joke_type='any', safe_mode=False)
    
    def get_knock_knock_joke(self) -> Dict:
        """
        Get a knock-knock joke.
        
        Returns:
            Dictionary containing knock-knock joke
        """
        return self.get_joke_from_jokeapi(category='Knock-Knock', joke_type='single')
    
    def get_pun_joke(self) -> Dict:
        """
        Get a pun joke.
        
        Returns:
            Dictionary containing pun joke
        """
        return self.get_joke_from_jokeapi(category='Pun', joke_type='any')
    
    def get_safe_joke(self) -> Dict:
        """
        Get a safe (family-friendly) joke.
        
        Returns:
            Dictionary containing safe joke
        """
        return self.get_joke_from_jokeapi(category='Any', joke_type='any', safe_mode=True)
    
    def get_joke_pair(self) -> Dict:
        """
        Get two jokes for comparison.
        
        Returns:
            Dictionary containing two jokes from different sources
        """
        joke1 = self.get_joke_from_jokeapi(category='Any')
        joke2 = self.get_joke_from_official_api()
        
        return {
            'joke_1': joke1,
            'joke_2': joke2,
            'comparison': 'Here are two jokes from different sources'
        }
    
    def get_random_joke(self) -> Dict:
        """
        Get a random joke from a random source.
        
        Returns:
            Dictionary containing random joke
        """
        sources = [self.get_joke_from_jokeapi, self.get_joke_from_official_api]
        selected_source = random.choice(sources)
        return selected_source()
    
    def search_jokes_by_category(self, category: str) -> Dict:
        """
        Search for jokes in a specific category.
        
        Args:
            category: Joke category
            
        Returns:
            Dictionary containing joke data
        """
        valid_categories = ['Any', 'General', 'Programming', 'Knock-Knock', 'Dark', 'Spooky', 'Pun']
        
        if category not in valid_categories:
            return {'error': f'Invalid category. Valid categories: {valid_categories}'}
        
        return self.get_joke_from_jokeapi(category=category)
    
    def get_jokes_batch(self, count: int = 5) -> List[Dict]:
        """
        Get multiple jokes at once.
        
        Args:
            count: Number of jokes to fetch
            
        Returns:
            List of joke dictionaries
        """
        jokes = []
        categories = ['Any', 'General', 'Programming', 'Pun', 'Knock-Knock']
        
        for i in range(count):
            category = random.choice(categories)
            joke = self.get_joke_from_jokeapi(category=category)
            if 'error' not in joke:
                jokes.append(joke)
        
        return jokes
    
    def format_joke_for_display(self, joke: Dict) -> str:
        """
        Format a joke for pretty display.
        
        Args:
            joke: Joke dictionary
            
        Returns:
            Formatted joke string
        """
        if 'error' in joke:
            return f"❌ Error: {joke['error']}"
        
        output = []
        output.append(f"\n{'='*70}")
        
        if 'source' in joke:
            output.append(f"📚 Source: {joke['source']}")
        
        if 'category' in joke:
            output.append(f"📂 Category: {joke['category']}")
        
        output.append(f"{'='*70}\n")
        
        # Handle different joke formats
        if joke.get('joke'):
            output.append(f"😂 {joke['joke']}")
        elif joke.get('setup') and joke.get('delivery'):
            output.append(f"🎤 Setup: {joke['setup']}")
            output.append(f"\n😂 Punchline: {joke['delivery']}")
        elif joke.get('setup') and joke.get('punchline'):
            output.append(f"🎤 Setup: {joke['setup']}")
            output.append(f"\n😂 Punchline: {joke['punchline']}")
        elif joke.get('full_joke'):
            output.append(f"😂 {joke['full_joke']}")
        
        # Add content warnings if applicable
        if joke.get('nsfw'):
            output.append("\n⚠️  Warning: This joke contains NSFW content")
        if joke.get('religious'):
            output.append("⚠️  Warning: This joke contains religious content")
        if joke.get('political'):
            output.append("⚠️  Warning: This joke contains political content")
        
        output.append(f"\n{'='*70}")
        
        return "\n".join(output)
    
    def print_joke(self, joke: Dict) -> None:
        """
        Print a formatted joke.
        
        Args:
            joke: Joke dictionary
        """
        print(self.format_joke_for_display(joke))
    
    def get_statistics(self) -> Dict:
        """
        Get statistics about available joke APIs.
        
        Returns:
            Dictionary containing API information
        """
        return {
            'available_sources': ['JokeAPI', 'Official Joke API'],
            'jokeapi_categories': ['Any', 'General', 'Programming', 'Knock-Knock', 'Dark', 'Spooky', 'Pun'],
            'jokeapi_types': ['single', 'twopart', 'any'],
            'features': [
                'Safe mode filtering',
                'Category selection',
                'Joke type filtering',
                'Batch retrieval',
                'Content warnings'
            ],
            'example_categories': {
                'Programming': 'Tech and code-related jokes',
                'Dark': 'Dark/edgy humor',
                'Knock-Knock': 'Classic knock-knock jokes',
                'Pun': 'Wordplay and puns',
                'General': 'General clean jokes'
            }
        }


def interactive_mode():
    """Run the joke generator in interactive mode."""
    generator = JokeGenerator()
    
    print("\n" + "="*70)
    print("  🎭 RANDOM JOKE GENERATOR")
    print("="*70)
    print("\nWelcome to the Random Joke Generator!")
    print("\nCommands:")
    print("  '1' - Get a random joke")
    print("  '2' - Get a programming joke")
    print("  '3' - Get a dark joke")
    print("  '4' - Get a knock-knock joke")
    print("  '5' - Get a pun joke")
    print("  '6' - Get a safe (family-friendly) joke")
    print("  '7' - Get multiple jokes (batch)")
    print("  '8' - Search by category")
    print("  '9' - Get two jokes from different sources")
    print("  '10' - View statistics")
    print("  'quit' - Exit\n")
    
    while True:
        try:
            user_input = input("Select an option (1-10 or 'quit'): ").strip().lower()
            
            if user_input == 'quit':
                print("\n👋 Thanks for laughing with us! Goodbye! 😄\n")
                break
            
            elif user_input == '1':
                print("\n⏳ Fetching a random joke...")
                joke = generator.get_random_joke()
                generator.print_joke(joke)
            
            elif user_input == '2':
                print("\n⏳ Fetching a programming joke...")
                joke = generator.get_programming_joke()
                generator.print_joke(joke)
            
            elif user_input == '3':
                print("\n⏳ Fetching a dark joke...")
                joke = generator.get_dark_joke()
                generator.print_joke(joke)
            
            elif user_input == '4':
                print("\n⏳ Fetching a knock-knock joke...")
                joke = generator.get_knock_knock_joke()
                generator.print_joke(joke)
            
            elif user_input == '5':
                print("\n⏳ Fetching a pun joke...")
                joke = generator.get_pun_joke()
                generator.print_joke(joke)
            
            elif user_input == '6':
                print("\n⏳ Fetching a safe joke...")
                joke = generator.get_safe_joke()
                generator.print_joke(joke)
            
            elif user_input == '7':
                count_input = input("How many jokes would you like? (default: 5): ").strip()
                count = int(count_input) if count_input.isdigit() else 5
                print(f"\n⏳ Fetching {count} jokes...")
                jokes = generator.get_jokes_batch(count)
                for i, joke in enumerate(jokes, 1):
                    print(f"\n📋 Joke {i}/{len(jokes)}")
                    generator.print_joke(joke)
            
            elif user_input == '8':
                print("\nAvailable categories:")
                print("  - Any, General, Programming, Knock-Knock, Dark, Spooky, Pun")
                category = input("Enter category: ").strip()
                print(f"\n⏳ Fetching a {category} joke...")
                joke = generator.search_jokes_by_category(category)
                generator.print_joke(joke)
            
            elif user_input == '9':
                print("\n⏳ Fetching two jokes from different sources...")
                result = generator.get_joke_pair()
                print("\n--- Joke from JokeAPI ---")
                generator.print_joke(result['joke_1'])
                print("\n--- Joke from Official Joke API ---")
                generator.print_joke(result['joke_2'])
            
            elif user_input == '10':
                stats = generator.get_statistics()
                print("\n" + "="*70)
                print("  📊 JOKE GENERATOR STATISTICS")
                print("="*70)
                print(f"\n🔗 Available Sources: {', '.join(stats['available_sources'])}")
                print(f"\n📂 Available Categories: {', '.join(stats['jokeapi_categories'])}")
                print(f"\n📝 Joke Types: {', '.join(stats['jokeapi_types'])}")
                print(f"\n✨ Features:")
                for feature in stats['features']:
                    print(f"   • {feature}")
                print(f"\n📚 Category Descriptions:")
                for category, description in stats['example_categories'].items():
                    print(f"   • {category}: {description}")
                print(f"\n{'='*70}\n")
            
            else:
                print("❌ Invalid option. Please select 1-10 or 'quit'.\n")
        
        except ValueError:
            print("❌ Invalid input. Please try again.\n")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! 😄\n")
            break


if __name__ == "__main__":
    interactive_mode()
