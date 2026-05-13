"""
Social Media Marketer Agent - Create social strategies and platform-specific content
Powered by Anthropic Claude
"""

from anthropic import Anthropic
import json
from typing import Optional, List, Dict

class SocialMediaMarketerAgent:
    """AI Agent for social media marketing and strategy."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Social Media Marketer Agent."""
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.model = "claude-3-5-sonnet-20241022"
        
        self.system_prompt = """You are an expert social media marketer with 12+ years of experience across all major platforms.
You specialize in:
- Platform-specific strategy (TikTok, Instagram, LinkedIn, Twitter/X, Facebook, YouTube Shorts)
- Community management and engagement
- Viral content creation
- Influencer partnerships and collaborations
- Social media analytics and optimization
- Paid social advertising strategy
- Crisis management on social media
- Hashtag research and strategy
- Trend identification and exploitation
- Growth hacking and audience building
- Social commerce and conversions
- Brand voice and authenticity

Create data-driven strategies that build engaged communities and drive business results.
Always consider platform algorithms, timing, and audience behavior.
Provide specific, actionable tactics with metrics to track success."""
    
    def chat(self, user_message: str) -> str:
        """Send a message and get a response from the agent."""
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=3000,
            system=self.system_prompt,
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def create_social_media_strategy(self, business_type: str, target_audience: str,
                                    goals: List[str], current_followers: Dict[str, int]) -> str:
        """Create a comprehensive social media strategy."""
        goals_str = "\n".join([f"- {goal}" for goal in goals])
        followers_str = json.dumps(current_followers, indent=2)
        
        prompt = f"""Create a comprehensive 90-day social media strategy.

Business Type: {business_type}
Target Audience: {target_audience}
Current Followers:
{followers_str}

Goals:
{goals_str}

Provide a detailed strategy including:
1. Platform prioritization
2. Content pillars and themes
3. Posting schedule and frequency
4. Content mix recommendations
5. Hashtag strategy
6. Engagement plan
7. Influencer opportunities
8. Paid advertising strategy
9. Growth tactics and KPIs
10. 90-day content roadmap
11. Competitor analysis
12. Tools and resources
13. Team responsibilities
14. Risk management

Make it specific, actionable, and data-driven."""
        
        return self.chat(prompt)
    
    def create_post_series(self, platform: str, topic: str, num_posts: int = 5,
                          posting_style: str = "Educational") -> str:
        """Create a series of platform-optimized posts."""
        prompt = f"""Create a series of {num_posts} social media posts for {platform}.

Topic: {topic}
Posting Style: {posting_style}

For each post provide:
1. Complete post copy
2. Optimal posting time
3. Platform-optimized hashtags
4. Mention/tag suggestions
5. Call-to-action
6. Visual suggestions
7. Expected engagement metrics
8. Platform-specific formatting

Make them ready to post directly."""
        
        return self.chat(prompt)
    
    def hashtag_strategy(self, niche: str, target_audience: str) -> str:
        """Develop a hashtag strategy for growth."""
        prompt = f"""Create a comprehensive hashtag strategy.

Niche: {niche}
Target Audience: {target_audience}

Provide:
1. Primary hashtags (high volume)
2. Secondary hashtags (medium volume)
3. Niche hashtags (low volume, targeted)
4. Trending hashtags to monitor
5. Seasonal hashtags
6. Brand-specific hashtags
7. Hashtag rotation strategy
8. Performance benchmarks
9. A/B testing recommendations
10. Platform-specific strategies

Organize by platform (Instagram, TikTok, Twitter, etc.)"""
        
        return self.chat(prompt)
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []


def interactive_mode():
    """Run the agent in interactive mode."""
    agent = SocialMediaMarketerAgent()
    
    print("\n" + "="*70)
    print("  SOCIAL MEDIA MARKETER AGENT - Interactive Mode")
    print("="*70)
    print("\nWelcome! I'm your social media marketing expert.")
    print("\nCommands:")
    print("  'strategy' - Create social strategy")
    print("  'posts' - Create post series")
    print("  'hashtags' - Get hashtag strategy")
    print("  'clear' - Clear history")
    print("  'quit' - Exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n👋 Now go grow that audience! 📱🚀\n")
            break
        elif user_input.lower() == 'clear':
            agent.clear_history()
            print("✅ Conversation history cleared.\n")
        elif user_input.lower() == 'strategy':
            business = input("Business type: ")
            audience = input("Target audience: ")
            response = agent.create_social_media_strategy(business, audience, 
                                                         ["Growth", "Engagement"], 
                                                         {"Instagram": 1000})
        elif user_input.lower() == 'posts':
            platform = input("Platform (Instagram/TikTok/LinkedIn): ")
            topic = input("Topic: ")
            response = agent.create_post_series(platform, topic)
        elif user_input.lower() == 'hashtags':
            niche = input("Your niche: ")
            response = agent.hashtag_strategy(niche, "general")
        else:
            response = agent.chat(user_input)
        
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    interactive_mode()
