"""
Content Creator Agent - Generate SEO-optimized content and content strategies
Powered by Anthropic Claude
"""

from anthropic import Anthropic
from typing import Optional, List

class ContentCreatorAgent:
    """AI Agent for content creation and strategy."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Content Creator Agent."""
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.model = "claude-3-5-sonnet-20241022"
        
        self.system_prompt = """You are an expert content creator and strategist with 10+ years of experience.
You specialize in:
- Blog post and article writing
- SEO content optimization
- Content marketing strategy
- Copywriting and persuasive writing
- Email marketing and newsletters
- Sales pages and landing pages
- Video scripts and transcripts
- Social media content
- Podcast scripts
- Ebook and long-form content
- Content calendars and planning
- Audience research and personas
- Keyword research and optimization
- Content distribution strategy
- Analytics and performance measurement

Create compelling, valuable, and optimized content that engages audiences and drives results.
Always follow SEO best practices and consider the target audience.
Maintain consistent brand voice and quality standards."""
    
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
    
    def create_blog_post(self, topic: str, keywords: List[str], 
                        audience: str, word_count: int = 1500,
                        tone: str = "professional") -> str:
        """Create a blog post with SEO optimization."""
        keywords_str = ", ".join(keywords)
        
        prompt = f"""Write a comprehensive blog post with the following specifications:

Topic: {topic}
Target Keywords: {keywords_str}
Target Audience: {audience}
Word Count: {word_count}
Tone: {tone}

Include:
1. Compelling headline (H1)
2. Meta description (160 characters)
3. Engaging introduction
4. 3-5 main sections with subheadings (H2/H3)
5. Key takeaways or summary
6. Call-to-action
7. Internal linking suggestions
8. External resource links

Optimization requirements:
- Natural keyword placement (1-1.5% density)
- Readable sentences and paragraphs
- Clear formatting and structure
- Focus keywords in first 100 words
- Power words and emotional triggers
- Statistics and data points
- Practical examples
- SEO best practices throughout

Format as ready-to-publish content."""
        
        return self.chat(prompt)
    
    def create_content_calendar(self, niche: str, duration_weeks: int = 4,
                               posting_frequency: str = "3 per week") -> str:
        """Create a content calendar with themed posts."""
        prompt = f"""Create a {duration_weeks}-week content calendar for the {niche} niche.

Posting Frequency: {posting_frequency}

For each post, provide:
1. Date and day
2. Post title
3. Main topic and angle
4. Target keywords
5. Content type (blog, infographic, video, etc.)
6. Word count estimate
7. Call-to-action
8. Promotion channels
9. Related content links
10. Success metrics

Considerations:
- Mix of evergreen and trending content
- Seasonal relevance
- Audience pain points and interests
- Educational and entertaining balance
- Lead generation opportunities
- Sales funnel alignment
- SEO opportunity mapping
- Content repurposing suggestions

Provide in a clear, calendar-style format."""
        
        return self.chat(prompt)
    
    def keyword_research(self, niche: str, difficulty_level: str = "medium") -> str:
        """Conduct keyword research for content planning."""
        prompt = f"""Conduct comprehensive keyword research for the {niche} niche.

Difficulty Level: {difficulty_level}

Provide:
1. Primary target keywords (10-15)
2. Long-tail keywords (15-20)
3. Semantic variations
4. Question-based keywords
5. Local keywords (if applicable)
6. Competitor keywords to target
7. Keywords to avoid (high competition, low relevance)

For each keyword include:
- Search volume estimate
- Competition level
- Search intent (informational/transactional/navigational)
- Content format recommendation
- CPC (if applicable)
- Seasonal trends

Also provide:
- Keyword clusters (related keywords by topic)
- Content opportunity analysis
- Gap analysis vs. competitors
- Search trend insights
- User intent breakdown
- Recommended content strategy"""
        
        return self.chat(prompt)
    
    def create_sales_page(self, product_name: str, target_audience: str,
                         unique_selling_points: List[str], price: str) -> str:
        """Create a high-converting sales page copy."""
        usp_str = "\n".join([f"- {usp}" for usp in unique_selling_points])
        
        prompt = f"""Create persuasive sales page copy for:

Product: {product_name}
Target Audience: {target_audience}
Price: {price}
Unique Selling Points:
{usp_str}

Include:
1. Attention-grabbing headline
2. Subheadline with value proposition
3. Problem-agitate-solve framework
4. Benefits (not just features)
5. Social proof and testimonials placeholder
6. Product overview section
7. Feature breakdown
8. Price justification
9. Objection handling
10. Risk reversal / guarantee
11. Scarcity and urgency elements
12. Clear CTA buttons
13. FAQ section
14. Final persuasive closing

Techniques:
- Emotional triggers and desires
- Power words and active voice
- Specific benefits over features
- Storytelling and relatability
- Trust-building elements
- Micro-commitment steps
- Visual descriptions
- Urgency without being pushy

Format as complete, ready-to-use copy."""
        
        return self.chat(prompt)
    
    def create_email_sequence(self, campaign_type: str, num_emails: int = 5,
                             goal: str = "conversion") -> str:
        """Create an email marketing sequence."""
        prompt = f"""Create a {num_emails}-email marketing sequence.

Campaign Type: {campaign_type}
Primary Goal: {goal}

For each email, provide:
1. Subject line with open rate tips
2. Preview text
3. Email body copy
4. CTA (button and text)
5. Personalization opportunities
6. Send timing recommendation
7. Segmentation suggestions
8. A/B testing ideas
9. Expected metrics

Sequence structure:
- Email 1: Welcome/hook
- Email 2: Build trust/education
- Email 3: Address objections
- Email 4: Social proof/urgency
- Email 5: Final CTA

Include:
- Storytelling and narrative arc
- Benefit focus
- Clear value proposition
- Responsive design considerations
- Mobile optimization notes
- Compliance (CAN-SPAM, GDPR)
- Unsubscribe handling
- Follow-up strategy
- Analytics tracking points"""
        
        return self.chat(prompt)
    
    def create_video_script(self, topic: str, video_length: str, 
                           platform: str, tone: str = "friendly") -> str:
        """Create a script for video content."""
        prompt = f"""Create a video script for:

Topic: {topic}
Length: {video_length}
Platform: {platform}
Tone: {tone}

Include:
1. Hook/attention-grabber (first 3 seconds)
2. Introduction and topic overview
3. Main content (segmented into digestible chunks)
4. Examples and demonstrations
5. Key takeaways
6. Call-to-action
7. Outro

For each section:
- Exact speaking script
- Visual/B-roll suggestions
- Text overlay suggestions
- Timing notes
- Emphasis and tone directions
- Camera directions (if live action)
- Graphics/animation notes

Considerations:
- Platform best practices (YouTube, TikTok, etc.)
- Attention span management
- Clear and concise language
- Natural speech patterns
- Engagement moments
- Searchability keywords
- Thumbnail/thumbnail text ideas
- Description copy for platform"""
        
        return self.chat(prompt)
    
    def create_infographic_outline(self, topic: str, data_points: int = 5) -> str:
        """Create an outline for infographic content."""
        prompt = f"""Create an infographic outline for:

Topic: {topic}
Number of Key Points: {data_points}

Provide:
1. Title and main headline
2. Subtitle/hook
3. Key data points and statistics
4. Visual layout suggestions
5. Color scheme recommendations
6. Icon and graphic suggestions
7. Typography recommendations
8. Data visualization types (charts, graphs, etc.)
9. Flow and logical progression
10. Call-to-action placement

For each element:
- Exact text/numbers
- Visual representation idea
- Data source/citation
- Emphasis techniques

Also include:
- Key message
- Target audience considerations
- Platform size recommendations
- Social sharing optimization
- Alt text for accessibility
- Design software recommendations"""
        
        return self.chat(prompt)
    
    def content_audit(self, topic: str, num_competitors: int = 3) -> str:
        """Audit competitor content for opportunities."""
        prompt = f"""Conduct a content audit for the {topic} niche.

Analyze {num_competitors} top competitors.

Provide:
1. Competitor content analysis
   - Most popular content pieces
   - Topics and formats
   - Engagement metrics
   - Content gaps

2. Content opportunity matrix
   - High-opportunity topics
   - Underserved keywords
   - Emerging trends
   - Audience pain points not addressed

3. Content strategy recommendations
   - Content types to prioritize
   - Topics to tackle
   - Unique angles to take
   - SEO opportunities

4. Competitive advantages to leverage
   - Unique expertise
   - Different perspectives
   - Underserved formats
   - Audience segments

5. Content recommendations (top 10)
   - Title suggestions
   - Keyword targeting
   - Format recommendations
   - Estimated traffic potential

Include:
- SWOT analysis for content
- Trend analysis
- Audience sentiment
- Backlink opportunities
- Collaboration possibilities"""
        
        return self.chat(prompt)
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []


def interactive_mode():
    """Run the agent in interactive mode."""
    agent = ContentCreatorAgent()
    
    print("\n" + "="*70)
    print("  CONTENT CREATOR AGENT - Interactive Mode")
    print("="*70)
    print("\nWelcome! I'm your content creation expert. Ask about:")
    print("  • Blog post writing")
    print("  • Content calendars")
    print("  • Keyword research")
    print("  • Sales page copywriting")
    print("  • Email sequences")
    print("  • Video scripts")
    print("  • Infographics")
    print("  • Content audits")
    print("\nCommands:")
    print("  'blog' - Create blog post")
    print("  'calendar' - Content calendar")
    print("  'keywords' - Keyword research")
    print("  'sales' - Sales page")
    print("  'email' - Email sequence")
    print("  'video' - Video script")
    print("  'infographic' - Infographic outline")
    print("  'audit' - Content audit")
    print("  'clear' - Clear history")
    print("  'quit' - Exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n👋 Keep creating great content! ✍️🚀\n")
            break
        elif user_input.lower() == 'clear':
            agent.clear_history()
            print("✅ Conversation history cleared.\n")
        elif user_input.lower() == 'blog':
            topic = input("Topic: ")
            response = agent.create_blog_post(topic, [topic], "general audience")
        elif user_input.lower() == 'calendar':
            niche = input("Niche: ")
            response = agent.create_content_calendar(niche)
        elif user_input.lower() == 'keywords':
            niche = input("Niche: ")
            response = agent.keyword_research(niche)
        elif user_input.lower() == 'sales':
            product = input("Product name: ")
            audience = input("Target audience: ")
            response = agent.create_sales_page(product, audience, ["Great value"], "$99")
        elif user_input.lower() == 'email':
            campaign = input("Campaign type: ")
            response = agent.create_email_sequence(campaign)
        elif user_input.lower() == 'video':
            topic = input("Topic: ")
            response = agent.create_video_script(topic, "5 minutes", "YouTube")
        elif user_input.lower() == 'infographic':
            topic = input("Topic: ")
            response = agent.create_infographic_outline(topic)
        elif user_input.lower() == 'audit':
            topic = input("Topic: ")
            response = agent.content_audit(topic)
        else:
            response = agent.chat(user_input)
        
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    interactive_mode()
