"""
WordPress Builder Agent - Automate WordPress site creation and management
Powered by Anthropic Claude
"""

from anthropic import Anthropic
from typing import Optional, List

class WordPressBuilderAgent:
    """AI Agent for WordPress site building and management."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the WordPress Builder Agent."""
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.model = "claude-3-5-sonnet-20241022"
        
        self.system_prompt = """You are an expert WordPress developer and site architect with 15+ years of experience.
You specialize in:
- WordPress site architecture and planning
- Theme selection and customization
- Plugin recommendations and configuration
- Performance optimization and caching
- Security hardening and best practices
- SEO optimization
- Conversion rate optimization
- WordPress multisite setups
- REST API integration
- WooCommerce configuration
- User management and roles
- Backup and disaster recovery
- Migration strategies
- Custom plugin development guidance

Provide expert recommendations that consider scalability, security, performance, and maintainability.
Always explain why specific choices are recommended."""
    
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
    
    def get_wordpress_setup_plan(self, requirements: str) -> str:
        """Get a complete WordPress setup plan based on requirements."""
        prompt = f"""Create a comprehensive WordPress setup plan for:
{requirements}

Include:
1. Site architecture and structure
2. Theme recommendations (with pros/cons)
3. Essential plugins list (with justification)
4. Security measures
5. Performance optimization strategy
6. SEO setup checklist
7. Backup and maintenance plan
8. User roles and permissions structure
9. Content organization strategy
10. Scalability considerations
11. Cost analysis
12. Implementation timeline
13. Tools and hosting recommendations
14. Training requirements"""
        
        return self.chat(prompt)
    
    def recommend_plugins(self, site_type: str, features_needed: List[str]) -> str:
        """Get plugin recommendations based on site type and features."""
        features_str = "\n".join([f"- {feature}" for feature in features_needed])
        
        prompt = f"""Recommend WordPress plugins for:
Site Type: {site_type}
Required Features:
{features_str}

For each recommendation provide:
1. Plugin name
2. Primary purpose
3. Why it's the best choice
4. Configuration tips
5. Performance impact
6. Cost (free/premium)
7. Alternatives
8. Potential conflicts to watch for
9. Essential settings
10. Best practices for implementation

Also include:
- Plugins to avoid
- Plugin conflicts to watch for
- Performance considerations
- Security implications
- Update frequency and reliability"""
        
        return self.chat(prompt)
    
    def security_hardening(self) -> str:
        """Get WordPress security hardening recommendations."""
        prompt = """Provide a comprehensive WordPress security hardening guide.

Cover:
1. Essential security plugins
2. Server-level security
3. WordPress core hardening
4. User management security
5. Database security
6. File permissions
7. SSL/HTTPS setup
8. Firewall configuration
9. Two-factor authentication
10. Backup security
11. Monitoring and alerts
12. Incident response plan
13. Regular security checklist
14. Security audit process
15. Common vulnerabilities and fixes

Provide specific, actionable steps with code examples where applicable."""
        
        return self.chat(prompt)
    
    def performance_optimization(self, current_issues: str = "") -> str:
        """Get WordPress performance optimization strategies."""
        prompt = f"""Create a WordPress performance optimization plan.
{f'Current issues: {current_issues}' if current_issues else ''}

Include:
1. Caching strategy (page, object, database, browser)
2. Image optimization techniques
3. CSS and JavaScript optimization
4. Database optimization
5. Content Delivery Network (CDN) setup
6. Plugin optimization
7. Theme optimization
8. Server configuration
9. Database indexing
10. Query optimization
11. Lazy loading implementation
12. Minification and compression
13. Performance monitoring tools
14. Benchmarking metrics
15. Step-by-step implementation

For each optimization, provide expected performance improvement."""
        
        return self.chat(prompt)
    
    def seo_optimization(self, niche: str, target_keywords: List[str]) -> str:
        """Get WordPress SEO optimization recommendations."""
        keywords_str = ", ".join(target_keywords)
        
        prompt = f"""Create a comprehensive WordPress SEO optimization plan.

Niche: {niche}
Target Keywords: {keywords_str}

Cover:
1. SEO plugin recommendations
2. Technical SEO setup
3. On-page SEO best practices
4. Keyword research and targeting
5. Content structure optimization
6. Internal linking strategy
7. XML sitemap setup
8. Robots.txt configuration
9. Schema markup implementation
10. Mobile optimization
11. Page speed optimization (Core Web Vitals)
12. Backlink strategy
13. Local SEO (if applicable)
14. SEO monitoring and analytics
15. Content calendar strategy

Provide specific WordPress plugins and configurations."""
        
        return self.chat(prompt)
    
    def woocommerce_setup(self, product_type: str, expected_volume: str) -> str:
        """Get WooCommerce setup and optimization recommendations."""
        prompt = f"""Create a comprehensive WooCommerce setup guide.

Product Type: {product_type}
Expected Volume: {expected_volume}

Include:
1. WooCommerce core setup
2. Payment gateway recommendations
3. Shipping configuration
4. Tax setup
5. Product catalog structure
6. Inventory management
7. Essential WooCommerce extensions
8. Security for e-commerce
9. Performance optimization for stores
10. Conversion optimization
11. Analytics and reporting
12. Customer management
13. Email automation
14. Abandoned cart recovery
15. Security and compliance

For each section, provide step-by-step instructions and best practices."""
        
        return self.chat(prompt)
    
    def migration_plan(self, from_platform: str, to_wordpress: str, timeline: str) -> str:
        """Create a WordPress migration plan."""
        prompt = f"""Create a detailed WordPress migration plan.

Migrating from: {from_platform}
To: {to_wordpress}
Timeline: {timeline}

Include:
1. Pre-migration checklist
2. Data export strategy
3. WordPress setup preparation
4. Content migration process
5. URL structure and redirects
6. SEO preservation strategy
7. User data migration
8. Testing plan
9. Backup and rollback strategy
10. DNS and domain cutover
11. Performance verification
12. Analytics and tracking setup
13. Monitoring after migration
14. Troubleshooting guide
15. Post-migration optimization

Provide tools, scripts, and detailed instructions."""
        
        return self.chat(prompt)
    
    def troubleshoot_issue(self, issue_description: str) -> str:
        """Get troubleshooting help for WordPress issues."""
        prompt = f"""Help troubleshoot this WordPress issue:
{issue_description}

Provide:
1. Likely causes
2. Diagnostic steps
3. Solutions (from simplest to most complex)
4. Code snippets if needed
5. Plugin recommendations
6. Prevention strategies
7. When to contact support
8. Relevant documentation links

Be specific and actionable."""
        
        return self.chat(prompt)
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []


def interactive_mode():
    """Run the agent in interactive mode."""
    agent = WordPressBuilderAgent()
    
    print("\n" + "="*70)
    print("  WORDPRESS BUILDER AGENT - Interactive Mode")
    print("="*70)
    print("\nWelcome! I'm your WordPress expert. Ask about:")
    print("  • Site setup and planning")
    print("  • Plugin recommendations")
    print("  • Security hardening")
    print("  • Performance optimization")
    print("  • SEO setup")
    print("  • WooCommerce configuration")
    print("  • Site migration")
    print("  • Troubleshooting")
    print("\nCommands:")
    print("  'plan' - Get setup plan")
    print("  'plugins' - Plugin recommendations")
    print("  'security' - Security hardening")
    print("  'performance' - Performance optimization")
    print("  'seo' - SEO setup")
    print("  'woocommerce' - WooCommerce setup")
    print("  'migrate' - Migration plan")
    print("  'clear' - Clear history")
    print("  'quit' - Exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n👋 Happy building! 🚀\n")
            break
        elif user_input.lower() == 'clear':
            agent.clear_history()
            print("✅ Conversation history cleared.\n")
        elif user_input.lower() == 'plan':
            req = input("What's your site about? ")
            response = agent.get_wordpress_setup_plan(req)
        elif user_input.lower() == 'plugins':
            site_type = input("Site type: ")
            response = agent.recommend_plugins(site_type, ["General"])
        elif user_input.lower() == 'security':
            response = agent.security_hardening()
        elif user_input.lower() == 'performance':
            response = agent.performance_optimization()
        elif user_input.lower() == 'seo':
            niche = input("Your niche: ")
            response = agent.seo_optimization(niche, ["your keyword"])
        elif user_input.lower() == 'woocommerce':
            ptype = input("Product type: ")
            response = agent.woocommerce_setup(ptype, "moderate")
        elif user_input.lower() == 'migrate':
            from_p = input("From (e.g., Wix): ")
            response = agent.migration_plan(from_p, "WordPress", "2 weeks")
        else:
            response = agent.chat(user_input)
        
        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    interactive_mode()
