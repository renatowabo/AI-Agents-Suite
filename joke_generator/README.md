# Random Joke Generator 🎭

A powerful, interactive joke generator that fetches jokes from multiple external APIs. Get unlimited laughs with support for various joke categories, types, and safe filtering!

## Features

✅ **Multiple API Sources**
- JokeAPI (7 categories, 2 formats)
- Official Joke API (classic setup/punchline jokes)

✅ **Joke Categories**
- General
- Programming
- Knock-Knock
- Dark (edgy/adult humor)
- Spooky
- Pun (wordplay)
- Any (random)

✅ **Content Filtering**
- Safe mode (family-friendly)
- NSFW, religious, political, racist, sexist content warnings
- Batch retrieval of multiple jokes

✅ **Flexible Joke Formats**
- Single-line jokes
- Two-part setup/punchline jokes
- Mixed formats

✅ **Interactive CLI**
- Menu-driven interface
- Real-time API fetching
- Pretty formatted output
- Statistics and information

## Installation

### Prerequisites
```bash
python 3.7+
requests library
```

### Setup

1. **Clone or download** the joke generator files

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Run the generator:**
   ```bash
   python joke_generator.py
   ```

## Quick Start

### Interactive Mode

```bash
python joke_generator.py
```

Then select from the menu:
```
1 - Get a random joke
2 - Get a programming joke
3 - Get a dark joke
4 - Get a knock-knock joke
5 - Get a pun joke
6 - Get a safe (family-friendly) joke
7 - Get multiple jokes (batch)
8 - Search by category
9 - Get two jokes from different sources
10 - View statistics
quit - Exit
```

### Programmatic Usage

```python
from joke_generator import JokeGenerator

# Initialize generator
generator = JokeGenerator()

# Get a random joke
joke = generator.get_random_joke()
generator.print_joke(joke)

# Get a programming joke
prog_joke = generator.get_programming_joke()
generator.print_joke(prog_joke)

# Get a safe joke
safe_joke = generator.get_safe_joke()
generator.print_joke(safe_joke)

# Get multiple jokes
jokes = generator.get_jokes_batch(count=5)
for joke in jokes:
    generator.print_joke(joke)
```

## API Methods

### Main Methods

#### `get_joke_from_jokeapi(category="Any", joke_type="any", safe_mode=False)`
Fetch a joke from JokeAPI with category and type filtering.

**Parameters:**
- `category`: "Any", "General", "Programming", "Knock-Knock", "Dark", "Spooky", "Pun"
- `joke_type`: "single", "twopart", "any"
- `safe_mode`: Boolean for family-friendly filtering

**Returns:** Dictionary with joke data

```python
joke = generator.get_joke_from_jokeapi(
    category="Programming",
    joke_type="twopart",
    safe_mode=True
)
```

#### `get_joke_from_official_api(joke_type="random")`
Fetch a joke from the Official Joke API.

**Parameters:**
- `joke_type`: "random" for any joke

**Returns:** Dictionary with joke data

```python
joke = generator.get_joke_from_official_api()
```

### Convenience Methods

```python
# Specific category jokes
generator.get_programming_joke()      # Tech jokes
generator.get_dark_joke()             # Dark humor
generator.get_knock_knock_joke()      # Knock-knock jokes
generator.get_pun_joke()              # Puns and wordplay

# Safe jokes (family-friendly)
generator.get_safe_joke()

# Multiple jokes
generator.get_jokes_batch(count=5)    # Get 5 random jokes

# Random from any source
generator.get_random_joke()

# Compare sources
generator.get_joke_pair()             # 2 jokes from different APIs

# Search by category
generator.search_jokes_by_category("Pun")
```

### Utility Methods

```python
# Format joke for display
formatted = generator.format_joke_for_display(joke)

# Print formatted joke
generator.print_joke(joke)

# Get API statistics
stats = generator.get_statistics()
```

## Response Format

### Single Joke Response
```python
{
    'source': 'JokeAPI',
    'category': 'Programming',
    'type': 'single',
    'joke': 'Why do programmers prefer dark mode? Because light attracts bugs!',
    'nsfw': False,
    'religious': False,
    'political': False,
    'racist': False,
    'sexist': False
}
```

### Two-Part Joke Response
```python
{
    'source': 'JokeAPI',
    'category': 'Knock-Knock',
    'type': 'twopart',
    'setup': 'Knock knock',
    'delivery': "Who's there? A programmer who's never heard of this category!",
    'nsfw': False,
    'religious': False,
    'political': False,
    'racist': False,
    'sexist': False
}
```

## Examples

### Example 1: Get a Random Programming Joke

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
joke = generator.get_programming_joke()
generator.print_joke(joke)
```

Output:
```
======================================================================
📚 Source: JokeAPI
📂 Category: Programming
======================================================================

😂 Why do programmers prefer dark mode? Because light attracts bugs!

======================================================================
```

### Example 2: Get Safe Jokes for the Family

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
jokes = generator.get_jokes_batch(count=3)

for i, joke in enumerate(jokes, 1):
    print(f"\nJoke {i}:")
    generator.print_joke(joke)
```

### Example 3: Search by Category

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

categories = ['Programming', 'Pun', 'Dark']

for category in categories:
    joke = generator.search_jokes_by_category(category)
    print(f"\n--- {category} Joke ---")
    generator.print_joke(joke)
```

### Example 4: Get Statistics

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
stats = generator.get_statistics()

print(f"Available sources: {stats['available_sources']}")
print(f"Categories: {stats['jokeapi_categories']}")
print(f"Features: {stats['features']}")
```

### Example 5: Error Handling

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
joke = generator.get_joke_from_jokeapi(category="Invalid")

if 'error' in joke:
    print(f"Error: {joke['error']}")
else:
    generator.print_joke(joke)
```

## API Information

### JokeAPI
- **Endpoint:** https://v2.jokeapi.dev/joke
- **Rate Limit:** Generous, no authentication needed
- **Categories:** 7 (Any, General, Programming, Knock-Knock, Dark, Spooky, Pun)
- **Formats:** Single-line or two-part
- **Features:** Content filtering, safe mode

### Official Joke API
- **Endpoint:** https://official-joke-api.appspot.com
- **Rate Limit:** Unlimited
- **Format:** Setup/punchline
- **Coverage:** 200+ jokes

## Content Warnings

The generator automatically detects and warns about:
- 🔞 **NSFW** - Explicit content
- 🙏 **Religious** - Religious references
- 🏛️ **Political** - Political content
- ⚠️ **Racist** - Potentially offensive content
- ⚠️ **Sexist** - Potentially offensive content

Use `safe_mode=True` to filter out content with warnings.

## Error Handling

The generator handles network errors gracefully:

```python
joke = generator.get_random_joke()

if 'error' in joke:
    print(f"Error: {joke['error']}")
    # Retry or use fallback
else:
    generator.print_joke(joke)
```

## Common Issues

### Issue: "ModuleNotFoundError: No module named 'requests'"
**Solution:**
```bash
pip install requests
```

### Issue: "Connection timeout" or "Failed to fetch joke"
**Solution:**
- Check your internet connection
- APIs might be temporarily unavailable
- The generator will try again on next request

### Issue: "No jokes found for this category"
**Solution:**
- Check that the category is spelled correctly
- Try a different category
- Use "Any" for broadest selection

## Customization

### Extend with Custom Jokes

```python
from joke_generator import JokeGenerator

class CustomJokeGenerator(JokeGenerator):
    def get_custom_joke(self):
        return {
            'source': 'Custom',
            'joke': 'Your custom joke here!'
        }

generator = CustomJokeGenerator()
joke = generator.get_custom_joke()
generator.print_joke(joke)
```

### Add a New API Source

```python
def get_joke_from_custom_api(self):
    try:
        response = requests.get('https://your-api-endpoint', 
                              headers=self.headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        return {
            'source': 'Custom API',
            'joke': data['joke']
        }
    except Exception as e:
        return {'error': f'Failed to fetch: {str(e)}'}
```

## Performance Tips

1. **Batch Retrieval** - Get multiple jokes at once to reduce API calls
2. **Caching** - Cache jokes locally to avoid redundant requests
3. **Category Selection** - Use specific categories instead of "Any" for faster retrieval
4. **Timeout** - Default timeout is 5 seconds, adjust if needed

## License

MIT License - Feel free to use and modify

## Credits

- **JokeAPI** - https://jokeapi.dev
- **Official Joke API** - https://github.com/15Dkk/official_joke_api
- Built with Python and the Requests library

## Support

For issues and questions:
1. Check error messages in the console
2. Verify internet connection
3. Try different joke categories
4. Review the examples above

---

**Now go make someone laugh! 😂**
