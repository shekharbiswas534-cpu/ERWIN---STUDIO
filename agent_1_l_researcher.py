"""
========================================================================================
MODULE: AGENT 1 - "L" (MASTER YOUTUBE STRATEGIC RESEARCHER)
SYSTEM: ERWIN AUTONOMOUS STUDIO PIPELINE
STANDARD: WORLD TOP 0.1% YOUTUBE PACKAGING & RETENTION ARCHITECTURE
========================================================================================
CAPABILITIES:
1. Multi-Stage Competitive Intelligence & Deep Trend Mining.
2. Real-time YouTube / Search Interest Scraping (Zero Cost, No Paid API Keys).
3. 5-Angle Psychological Curiosity Gap Modeling.
4. Retention Curve Drop-off Prevention Blueprint (First 30 Seconds).
5. Comprehensive JSON Output for Agent 2 (Rohan - Scriptwriter) & Agent 6 (Senku - Thumbnail).
========================================================================================
"""

import os
import sys
import json
import time
import urllib.parse
from datetime import datetime
import requests


class YouTubeSearchScraper:
    """
    Simulates real-world search intent extraction via YouTube & Google autocomplete
    without requiring expensive scraping credits or paid API keys.
    """
    @staticmethod
    def get_search_suggestions(query, country="US"):
        url = f"https://suggestqueries.google.com/complete/search?client=youtube&ds=yt&gl={country}&q={urllib.parse.quote(query)}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        try:
            res = requests.get(url, headers=headers, timeout=10)
            if res.status_code == 200:
                # Raw text format: window.google.ac.h(["query",[["sugg1",0],["sugg2",0]]...])
                raw = res.text
                start = raw.find("(")
                end = raw.rfind(")")
                if start != -1 and end != -1:
                    data = json.loads(raw[start+1:end])
                    return [item[0] for item in data[1]]
        except Exception as e:
            print(f"[!] Warning: Autocomplete fetch failed: {e}")
        return []


class MarketIntelligenceEngine:
    """
    Regional economic and behavioral intelligence for faceless channels worldwide.
    """
    MARKET_DATA = {
        "USA": {
            "expected_cpm": "$18 - $42",
            "viewer_attention_span": "Ultra-low (0-3.5 seconds decision window)",
            "primary_drivers": ["Financial Sovereignty", "High Stakes Outrage", "Elite Lifestyle Voyeurism", "Shocking Hidden Truths"],
            "banned_tropes": ["Slow montage intros", "'In this video we will discuss'", "Uncurated AI robot voices"]
        },
        "UK": {
            "expected_cpm": "$14 - $30",
            "viewer_attention_span": "Moderate (Requires journalistic grounding)",
            "primary_drivers": ["Understated Irony", "Systemic Scandals", "Historical Deceptions", "Wealth Discrepancies"],
            "banned_tropes": ["Over-hyped screaming intros", "Cartoon sound spam"]
        },
        "GLOBAL_TIER_1": {
            "expected_cpm": "$12 - $26",
            "viewer_attention_span": "Short-form trained visual appetite",
            "primary_drivers": ["Mind-bending Facts", "Universal Power Dynamics", "Extreme Wealth Contrast"],
            "banned_tropes": ["Heavy colloquial local slang without visual subtitles"]
        }
    }

    @classmethod
    def get_demographics(cls, country):
        c = country.upper()
        return cls.MARKET_DATA.get(c, cls.MARKET_DATA["GLOBAL_TIER_1"])


class AgentLMasterResearcher:
    """
    Master YouTube Researcher 'L'.
    Executes a 4-phase research breakdown rivaling premier YouTube packaging agencies.
    """
    def __init__(self, api_key=None, memory_dir="studio_pipeline"):
        self.agent_name = "L"
        self.designation = "Master YouTube Researcher & Algorithmic Strategist"
        self.api_key = api_key or os.getenv("GEMINI_KEY")
        self.memory_dir = memory_dir
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

        if not self.api_key:
            raise ValueError("[L Fatal Error] GEMINI_KEY missing! Kripya API key pass karein.")

        os.makedirs(self.memory_dir, exist_ok=True)

    def _execute_ai_reasoning(self, system_prompt, user_content):
        url = f"{self.base_url}?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"parts": [{"text": user_content}]}],
            "generationConfig": {
                "response_mime_type": "application/json",
                "temperature": 0.4,
                "topP": 0.95
            }
        }

        for attempt in range(3):
            try:
                res = requests.post(url, headers=headers, json=payload, timeout=75)
                if res.status_code == 200:
                    raw_text = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                    return json.loads(raw_text)
                else:
                    print(f"[!] L API Retry ({attempt+1}/3): Status {res.status_code} - {res.text}")
                    time.sleep(2)
            except Exception as ex:
                print(f"[!] L Connection glitch ({attempt+1}/3): {ex}")
                time.sleep(3)

        raise RuntimeError("[L Fatal] Failed to generate strategic intelligence after 3 attempts.")

    def run_deep_research(self, niche_or_topic, target_country="USA", channel_id="CH_GENERAL"):
        print(f"\n========================================================")
        print(f"🕵️‍♂️ [L: MASTER RESEARCH ENGAGED]")
        print(f"Target: '{niche_or_topic}' | Country: {target_country} | Channel: {channel_id}")
        print(f"========================================================")

        # Phase 1: Live Autocomplete & Search Intent Mining
        print(f"[*] Phase 1: Scraping YouTube search intents for real search trends...")
        scraped_queries = YouTubeSearchScraper.get_search_suggestions(niche_or_topic, country=target_country[:2])
        print(f"    -> Extracted {len(scraped_queries)} real audience search intents.")

        # Phase 2: Market Economics & Viewer Psychology Modeling
        market_intel = MarketIntelligenceEngine.get_demographics(target_country)

        # Phase 3: Strategic Deep Synthesis via L's Persona
        print(f"[*] Phase 2: Formulating high-CTR packaging matrices & drop-off blueprints...")
        system_instruction = f"""
You are L Lawliet, the legendary master detective, operating exclusively as the world's most sophisticated YouTube Research Strategist for elite faceless channels.
You answer directly to Commander Erwin.

YOUR RESEARCH PARADIGM:
1. No cliches or generic summaries. Everything must be engineered for extreme Click-Through-Rate (CTR) and 65%+ Audience Retention.
2. Target Market Intelligence ({target_country}):
   - Projected CPM: {market_intel['expected_cpm']}
   - Viewer Psychology: {', '.join(market_intel['primary_drivers'])}
   - Strictly Forbidden: {', '.join(market_intel['banned_tropes'])}
3. 5-ANGLE TITLE PSYCHOLOGY:
   Every concept must provide 5 distinct title options:
   * Angle A: Curiosity Gap (Missing information)
   * Angle B: High-Stakes / Extreme Consequence
   * Angle C: Negative Bias / Paranoia (Why X is wrong)
   * Angle D: Secret Authority / Insider Whistleblower
   * Angle E: Counter-Intuitive Paradox
4. RETENTION BLUEPRINT (0-30s):
   * 0-5s: Visual anchor + Spoken Pattern Interrupt
   * 5-15s: Micro-Hook + High Stakes Premise
   * 15-30s: Open Loop Creation (What they will lose if they click away)
5. COMPETITOR DEFECT ANALYSIS:
   Expose why current top YouTube videos on this topic bleed viewers, and give the exact counter-strategy.

OUTPUT SPECIFICATION:
You must output STRICT, VALID JSON ONLY. Zero markdown wrapping outside the JSON. Follow this exact industrial schema:
{{
  "metadata": {{
    "researcher": "L (YouTube Strategic Researcher)",
    "timestamp_utc": "{datetime.utcnow().isoformat()}",
    "channel_id": "{channel_id}",
    "investigated_niche": "{niche_or_topic}",
    "target_geography": "{target_country}",
    "projected_cpm": "{market_intel['expected_cpm']}"
  }},
  "scraped_search_intents": {json.dumps(scraped_queries)},
  "competitor_vulnerabilities": [
    {{
      "common_mistake": "string",
      "our_counter_attack": "string"
    }}
  ],
  "master_video_blueprints": [
    {{
      "concept_rank": 1,
      "strategic_working_title": "string (Maximum virality)",
      "title_matrix_5_angles": {{
        "curiosity_gap": "string",
        "high_stakes": "string",
        "negative_bias": "string",
        "insider_whistleblower": "string",
        "counter_intuitive_paradox": "string"
      }},
      "target_ctr_projection": "8.5% - 14.0%",
      "packaging_score_out_of_100": 94,
      "first_30_seconds_retention_engineering": {{
        "visual_pattern_interrupt_0_to_5s": "Detailed visual cue description",
        "verbatim_spoken_script_0_to_5s": "Exact first 2 sentences spoken",
        "micro_stakes_escalation_5_to_15s": "Scene pacing & SFX cues",
        "open_loop_hook_15_to_30s": "Narrative loop that cannot be resolved until minute 7+"
      }},
      "narrative_3_act_beats": [
        "Act 1: The Disruption & Hidden Anomaly",
        "Act 2: The Systematic Investigation & Smoking Gun",
        "Act 3: The Terrifying / Aspirational Reality & Climax"
      ],
      "high_cpm_target_keywords": ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6"],
      "recommended_visual_tone": "Cinematic Dark / Bloomberg Infographics / Hypnotic Luxury",
      "pacing_speed_words_per_minute": 150
    }}
  ],
  "erwin_executive_summary": "Crisp 3-sentence summary for Commander Erwin explaining why this topic will dominate the algorithm."
}}
"""

        user_prompt = f"""
Conduct exhaustive YouTube strategic research for:
Niche: {niche_or_topic}
Target Region: {target_country}
Scraped Real Audience Queries: {scraped_queries[:8]}
Channel Category: {channel_id}

Deliver the Top 1 global-tier video concept with extreme depth, psychological hooks, and verbatim retention scripts.
"""

        result_data = self._execute_ai_reasoning(system_instruction, user_prompt)

        # Phase 4: Output Verification & Persistence
        output_filename = os.path.join(self.memory_dir, f"{channel_id}_research_data.json")
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2, ensure_ascii=False)

        print(f"\n[+] L Research Complete!")
        print(f"[+] Output locked and stored: {output_filename}")
        print(f"[+] Briefing to Commander Erwin: {result_data.get('erwin_executive_summary', 'Ready.')}")
        print(f"========================================================\n")

        return result_data


if __name__ == "__main__":
    # Test Runner for L
    key = os.getenv("GEMINI_KEY")
    if not key:
        key = input("Apni Gemini API Key paste karein: ").strip()

    if not key:
        print("[!] Key missing. Execution aborted.")
        sys.exit(1)

    researcher = AgentLMasterResearcher(api_key=key)

    print("\n--- [AGENT 1: 'L' STANDALONE TEST ROOM] ---")
    topic_input = input("Research Niche / Topic (e.g., Ultra Luxury Mansions / Unsolved Cold Cases / Dark Apple Marketing): ").strip() or "Billionaire Underground Bunkers"
    country_input = input("Target Country (Default: USA): ").strip() or "USA"
    channel_input = input("Channel ID (e.g. CH_01_LUXURY / CH_02_MYSTERY / CH_GENERAL): ").strip() or "CH_01_LUXURY"

    report = researcher.run_deep_research(topic_input, target_country=country_input, channel_id=channel_input)
    
    print("\n[Preview of L's Output Schema]:")
    print(f"Projected CPM: {report['metadata']['projected_cpm']}")
    print(f"Working Title: {report['master_video_blueprints'][0]['strategic_working_title']}")
    print(f"5-Angle Titles: {json.dumps(report['master_video_blueprints'][0]['title_matrix_5_angles'], indent=2)}")
    print(f"0-5s Hook Script: \"{report['master_video_blueprints'][0]['first_30_seconds_retention_engineering']['verbatim_spoken_script_0_to_5s']}\"")
