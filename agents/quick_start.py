"""
Quick Start Guide - Run all three agents with example usage
"""

from wordpress_builder.wordpress_builder_agent import WordPressBuilderAgent
from content_creator.content_creator_agent import ContentCreatorAgent
from social_media_marketer.social_media_marketer_agent import SocialMediaMarketerAgent

def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def main():
    """Main entry point."""
    print("\n" + "="*70)
    print("  AI AGENTS SUITE - Quick Start Guide")
    print("  WordPress Builder | Content Creator | Social Media Marketer")
    print("="*70)
    
    print("""
    Welcome to the AI Agents Suite! This tool provides three specialized AI agents:
    
    1️⃣  WordPress Builder Agent
       - Automate WordPress setup and management
       - Get plugin recommendations
       - Configure security and performance
    
    2️⃣  Content Creator Agent
       - Generate blog posts and articles
       - Create content calendars
       - Optimize for SEO
    
    3️⃣  Social Media Marketer Agent
       - Build comprehensive strategies
       - Create platform-specific content
       - Plan influencer collaborations
    
    Each agent uses Anthropic's Claude for intelligent automation.
    """)
    
    print("\n📋 MAIN MENU")
    print("  1. Run Interactive WordPress Builder Agent")
    print("  2. Run Interactive Content Creator Agent")
    print("  3. Run Interactive Social Media Marketer Agent")
    print("  4. Exit")
    
    choice = input("\nSelect an option (1-4): ").strip()
    
    if choice == "1":
        print("\n🚀 Starting WordPress Builder Agent...\n")
        from wordpress_builder.wordpress_builder_agent import interactive_mode
        interactive_mode()
    elif choice == "2":
        print("\n🚀 Starting Content Creator Agent...\n")
        from content_creator.content_creator_agent import interactive_mode
        interactive_mode()
    elif choice == "3":
        print("\n🚀 Starting Social Media Marketer Agent...\n")
        from social_media_marketer.social_media_marketer_agent import interactive_mode
        interactive_mode()
    elif choice == "4":
        print("\n👋 Goodbye! Happy creating with AI agents! 🚀")
    else:
        print("❌ Invalid option. Please select 1-4.")

if __name__ == "__main__":
    main()
