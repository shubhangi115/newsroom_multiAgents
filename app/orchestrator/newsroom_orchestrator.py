from app.agents.fact_checker import fact_check_agent
from app.agents.research_agent import research_agent
from app.agents.seo_agent import seo_agent
from app.agents.script_writer import script_writer_agent
from app.agents.image_prompt_agent import image_prompt_agent
from app.agents.video_prompt_agent import video_prompt_agent
from app.agents.headline_optimiser import headline_optimiser_agent
from app.agents.social_media_agent import social_media_agent
from app.agents.quality_validator import quality_validator_agent
from app.agents.final_editor import final_editor_agent



class NewsroomOrchestrator:

    async def run(self,topic: str,target_agent:str) -> dict:  # target_agent is used to select aganet 

        result = {
            "research": None,
            "fact_check": None,
            "seo": None,
            "script": None,
            "image": None,
            "video": None,
            "headline": None,
            "social_media": None,
            "validation": None,
            "final": None
        }

        print("Research...")
        research_report = await research_agent.run(
            topic=topic
        )
        result["research"] = research_report

        if target_agent == "research":
            return result

        # we are converting the research_report structured ResearchReport object into JSON text as fact_check_report expects input as str not ResearchReport object
        research_report_text = research_report.model_dump_json(
            indent=2 # indent=2 means "Use this many spaces for each indentation level.", to have the json in indentation instead of single line
        )

        # the above research_report_text we did due to test the reserach is returning json structured or not

        print("Fact Check...")
        fact_check_report = await fact_check_agent.run(
            # research_report=research_report_text # research_report_text instead of research_report
            research_report=research_report  # research_report_text instead of research_report
        )
        result["fact_check"] = fact_check_report

        if target_agent == "fact_check":
            return result


        print("SEO...")
        seo_report = await seo_agent.run(
            fact_check_report=fact_check_report
        )
        result["seo"] = seo_report
        
        if target_agent == "seo":
            return result

        print("Script...")
        script = await script_writer_agent.run(
            research_report=research_report,
            fact_check_report=fact_check_report,
            seo_report=seo_report
        )
        result["script"] = script
                
        if target_agent == "script":
            return result


        print("Image...")
        image_prompt = await image_prompt_agent.run(
            fact_check_report=fact_check_report,
            script=script
        )
        result["image"] = image_prompt
                        
        if target_agent == "image":
            return result


        print("Video...")
        video_prompt=await video_prompt_agent.run(
            fact_check_report=fact_check_report,
            script=script,
            image_prompt=image_prompt
        )
        result["video"] = video_prompt
                                
        if target_agent == "video":
            return result


        print("Headline...")
        headline_report= await headline_optimiser_agent.run(
            fact_check_report= fact_check_report,
            seo_report= seo_report,
            script= script
        )
        result["headline"] = headline_report
                                        
        if target_agent == "headline":
            return result
        

        print("Social...")
        media_report= await social_media_agent.run(
            fact_check_report= fact_check_report, 
            script= script, 
            headline_report= headline_report
        )
        result["social_media"] = media_report
                                                
        if target_agent == "social_media":
            return result
        

        print("Validation...")
        validation_report = await quality_validator_agent.run(
            research_report=research_report,
            fact_check_report=fact_check_report,
            seo_report=seo_report,
            script=script,
            image_prompt=image_prompt,
            video_prompt=video_prompt,
            headline_report=headline_report,
            social_media_report=media_report
        )
        result["validation"] = validation_report
                                                        
        if target_agent == "validation":
            return result


        print("Final...") 
        final_package = await final_editor_agent.run(
            fact_check_report=fact_check_report,
            seo_report=seo_report,
            script=script,
            image_prompt=image_prompt,
            video_prompt=video_prompt,
            headline_report=headline_report,
            social_media_report=media_report,
            validation_report=validation_report
        ) 
        result["final"] = final_package
                                                                
        if target_agent == "final":
            return result

        return {
            "research": research_report,
            "fact_check": fact_check_report,
            "seo": seo_report,
            "script": script,
            "image_prompt": image_prompt,
            "video_prompt": video_prompt,
            "headline": headline_report,
            "social_media": media_report,
            "validation": validation_report,
            "final": final_package
        }


newsroom_orchestrator = NewsroomOrchestrator()