from pydantic import BaseModel, Field

# for the frontned so the user can send the topic and which aegnt to run
class NewsroomRequest(BaseModel):
    topic: str
    target_agent: str

# for adding urls in the contnet
class ResearchSource(BaseModel):
    title: str
    url: str


# for the structured JSON format to return ,instead of single string 
class ResearchReport(BaseModel):
    topic_overview: str
    key_facts: list[str]
    important_organizations: list[str]
    relevant_dates_and_statistics: list[str]
    claims_requiring_verification: list[str]
    research_summary: str
    sources: list[ResearchSource] = Field(default_factory=list)

class FactCheckReport(BaseModel):
    claims_examined: list[str]
    supported_claims: list[str]
    claims_requiring_verification: list[str]
    unsupported_claims: list[str]
    overall_verdict: str

class SEOReport(BaseModel):
    seo_title: str
    meta_description: str
    primary_keywords: list[str]
    secondary_keywords: list[str]
    url_slug: str
    search_intent: str

class ScriptReport(BaseModel):
    headline: str
    lead: str
    body: str
    conclusion: str

class ImagePromptReport(BaseModel):
    image_concept: str
    image_type: str
    generation_prompt: str
    color_palette: str
    aspect_ratio: str
    elements_to_avoid: list[str]

class VideoPromptReport(BaseModel):
    video_concept: str
    video_style: str
    opening_scene: str
    scene_breakdown: str
    voiceover_direction: str
    transitions: str
    color_palette: str
    aspect_ratio: str
    elements_to_avoid: list[str]

class HeadlineReport(BaseModel):
    recommended_headline: str
    seo_headline: str
    breaking_news_headline: str
    mobile_friendly_headline: str
    reasoning: str

class SocialMediaReport(BaseModel):
    x_post: str
    linkedin_post: str
    instagram_caption: str
    facebook_post: str
    hashtags: list[str]
    call_to_action: str

class ValidationReport(BaseModel):
    overall_assessment: str
    research_and_article_consistency: str
    fact_check_compliance: str
    seo_and_headline_consistency: str
    visual_prompt_consistency: str
    social_media_consistency: str
    issues_found: list[str]
    recommended_changes: list[str]
    final_recommendation: str

class FinalReport(BaseModel):
    final_headline: str
    final_article: str
    final_seo_package: str
    final_image_prompt: str
    final_video_prompt: str
    final_social_media_package: str
    publication_notes: str
    publication_status: str

class ResearchRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=3,
        max_length=300,
        description="News topic that the Research Agent should investigate."
    )


# class ResearchResponse(BaseModel):
#     research: ResearchReport # as we have changed the return type of research agent to object 
#     fact_check: FactCheckReport
#     seo: SEOReport
#     script: ScriptReport
#     image_prompt: ImagePromptReport
#     video_prompt: VideoPromptReport
#     headline: HeadlineReport
#     social_media: SocialMediaReport
#     validation: ValidationReport
#     final: FinalReport  

# as the user can shoose any number of aganet
class ResearchResponse(BaseModel):
    research: ResearchReport | None = None
    fact_check: FactCheckReport | None = None
    seo: SEOReport | None = None
    script: ScriptReport | None = None
    image_prompt: ImagePromptReport | None = None
    video_prompt: VideoPromptReport | None = None
    headline: HeadlineReport | None = None
    social_media: SocialMediaReport | None = None
    validation: ValidationReport | None = None
    final: FinalReport | None = None

