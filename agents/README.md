# AI Agents Suite

Three powerful AI agents powered by **Anthropic Claude** for WordPress development, content creation, and social media marketing.

## 🤖 Agents Included

### 1. **WordPress Builder Agent**
Automate WordPress site creation and management with expert guidance on:
- Site architecture and planning
- Theme and plugin recommendations
- Security hardening
- Performance optimization
- SEO setup
- WooCommerce configuration
- Site migration
- Troubleshooting

**Run:** `python agents/wordpress_builder/wordpress_builder_agent.py`

### 2. **Content Creator Agent**
Generate SEO-optimized content with strategies for:
- Blog posts and articles
- Content calendars
- Keyword research
- Sales page copywriting
- Email marketing sequences
- Video scripts
- Infographic outlines
- Content audits

**Run:** `python agents/content_creator/content_creator_agent.py`

### 3. **Social Media Marketer Agent**
Build comprehensive social media strategies for:
- Multi-platform strategy development
- Platform-specific content creation
- Hashtag research and strategy
- Influencer partnership planning
- Paid social advertising
- Crisis management
- Growth hacking tactics
- Analytics and optimization

**Run:** `python agents/social_media_marketer/social_media_marketer_agent.py`

## 🚀 Quick Start

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r agents/requirements.txt
   ```

3. **Set up your API key:**
   ```bash
   cp agents/.env.example agents/.env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

   Get your API key from: https://console.anthropic.com/

### Run an Agent

**Interactive Mode:**
```bash
python agents/wordpress_builder/wordpress_builder_agent.py
python agents/content_creator/content_creator_agent.py
python agents/social_media_marketer/social_media_marketer_agent.py
```

**In Python Code:**
```python
from agents.wordpress_builder.wordpress_builder_agent import WordPressBuilderAgent

agent = WordPressBuilderAgent()
plan = agent.get_wordpress_setup_plan("E-commerce site selling digital products")
print(plan)
```

## 💡 Usage Examples

### WordPress Builder
```python
from agents.wordpress_builder.wordpress_builder_agent import WordPressBuilderAgent

agent = WordPressBuilderAgent()

# Get a complete setup plan
plan = agent.get_wordpress_setup_plan(
    requirements="Membership site with course content"
)

# Get plugin recommendations
plugins = agent.recommend_plugins(
    site_type="membership",
    features_needed=["User authentication", "Course delivery", "Payment processing"]
)

# Get security hardening guide
security = agent.security_hardening()

# Get performance optimization plan
perf = agent.performance_optimization()
```

### Content Creator
```python
from agents.content_creator.content_creator_agent import ContentCreatorAgent

agent = ContentCreatorAgent()

# Create a blog post
blog = agent.create_blog_post(
    topic="AI in Business",
    keywords=["artificial intelligence", "business automation", "AI tools"],
    audience="Business owners and managers",
    word_count=2000
)

# Create a content calendar
calendar = agent.create_content_calendar(
    niche="SaaS and business tools",
    duration_weeks=8,
    posting_frequency="3 per week"
)

# Conduct keyword research
keywords = agent.keyword_research(
    niche="Digital marketing",
    difficulty_level="medium"
)

# Create an email sequence
emails = agent.create_email_sequence(
    campaign_type="Product launch",
    num_emails=5,
    goal="conversion"
)
```

### Social Media Marketer
```python
from agents.social_media_marketer.social_media_marketer_agent import SocialMediaMarketerAgent

agent = SocialMediaMarketerAgent()

# Create a social media strategy
strategy = agent.create_social_media_strategy(
    business_type="SaaS startup",
    target_audience="Tech entrepreneurs",
    goals=["Increase brand awareness", "Drive website traffic"],
    current_followers={"LinkedIn": 5000, "Twitter": 2000}
)

# Create post series
posts = agent.create_post_series(
    platform="LinkedIn",
    topic="Remote work productivity tips",
    num_posts=7,
    posting_style="Professional with practical tips"
)

# Get hashtag strategy
hashtags = agent.hashtag_strategy(
    niche="Digital marketing",
    target_audience="Marketing professionals"
)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the `agents/` directory:

```
ANTHROPIC_API_KEY=your_api_key_here
MODEL=claude-3-5-sonnet-20241022
```

### Using Different Models

You can change the model in your code:

```python
agent = WordPressBuilderAgent()
agent.model = "claude-3-opus-20240229"  # Different model
```

Available models:
- `claude-3-5-sonnet-20241022` (recommended - best balance)
- `claude-3-opus-20240229` (most capable)
- `claude-3-haiku-20240307` (fastest, less capable)

## 📊 Features

✅ **Conversation Memory** - Agents remember previous messages for context
✅ **Specialized Methods** - Purpose-built functions for common tasks
✅ **Interactive CLI** - Chat interface for each agent
✅ **Programmatic API** - Use as Python modules in your code
✅ **Production-Ready** - Error handling and best practices
✅ **Flexible** - Customize prompts and parameters
✅ **Scalable** - Handle complex requests efficiently

## 🎯 Use Cases

### WordPress Builder
- Launch new WordPress sites
- Optimize existing sites
- Plan site migrations
- Get security recommendations
- Troubleshoot issues
- Plan WooCommerce setup

### Content Creator
- Write blog posts at scale
- Plan content calendars
- Research keywords
- Write sales copy
- Create email campaigns
- Script video content
- Audit competitor content

### Social Media Marketer
- Develop social strategies
- Create platform-specific posts
- Research hashtags
- Plan influencer partnerships
- Manage crisis communications
- Build growth plans
- Create paid ad strategies

## 📚 API Reference

### WordPressBuilderAgent Methods
- `get_wordpress_setup_plan(requirements)` - Get comprehensive setup plan
- `recommend_plugins(site_type, features_needed)` - Get plugin recommendations
- `security_hardening()` - Get security guide
- `performance_optimization(current_issues)` - Get optimization plan
- `seo_optimization(niche, target_keywords)` - Get SEO setup
- `woocommerce_setup(product_type, expected_volume)` - Get WooCommerce guide
- `migration_plan(from_platform, to_wordpress, timeline)` - Get migration plan
- `troubleshoot_issue(issue_description)` - Get troubleshooting help
- `chat(user_message)` - Send any message and get response
- `clear_history()` - Clear conversation history

### ContentCreatorAgent Methods
- `create_blog_post(topic, keywords, audience, word_count, tone)` - Create blog post
- `create_content_calendar(niche, duration_weeks, posting_frequency)` - Create calendar
- `keyword_research(niche, difficulty_level)` - Research keywords
- `create_sales_page(product_name, target_audience, unique_selling_points, price)` - Create sales copy
- `create_email_sequence(campaign_type, num_emails, goal)` - Create email series
- `create_video_script(topic, video_length, platform, tone)` - Create video script
- `create_infographic_outline(topic, data_points)` - Create infographic outline
- `content_audit(topic, num_competitors)` - Audit competitor content
- `chat(user_message)` - Send any message and get response
- `clear_history()` - Clear conversation history

### SocialMediaMarketerAgent Methods
- `create_social_media_strategy(business_type, target_audience, goals, current_followers)` - Create strategy
- `create_post_series(platform, topic, num_posts, posting_style)` - Create posts
- `hashtag_strategy(niche, target_audience)` - Get hashtag strategy
- `chat(user_message)` - Send any message and get response
- `clear_history()` - Clear conversation history

## 🔐 Security

- Never commit your `.env` file with API keys
- Keep your `ANTHROPIC_API_KEY` confidential
- Use appropriate access controls for your codebase
- Monitor your API usage and costs

## 💰 Pricing

Anthropic API charges based on input and output tokens. Check current pricing at:
https://www.anthropic.com/pricing

## 🤝 Contributing

Feel free to extend these agents with:
- Additional methods and capabilities
- Custom prompts for your use case
- Integration with other tools and APIs
- Enhanced error handling
- Additional agents for other domains

## 📖 Resources

- **Anthropic Documentation**: https://docs.anthropic.com
- **Claude API Reference**: https://docs.anthropic.com/en/api/messages
- **Best Practices**: https://docs.anthropic.com/en/docs/build-a-bot

## 📄 License

MIT License - Feel free to use in personal and commercial projects.

## 🚀 Next Steps

1. Get your Anthropic API key
2. Set up your `.env` file
3. Install dependencies
4. Run one of the agents
5. Explore the interactive mode
6. Integrate into your workflow

## 📞 Support

For issues and questions:
1. Check the agent's interactive help (type 'help' or 'quit')
2. Review the code comments
3. Consult Anthropic documentation
4. Experiment with different prompts

---

**Happy automating with AI! 🚀**
