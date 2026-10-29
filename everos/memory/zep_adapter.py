# APOSTLES TREEOFLIFE+ ANCESTORS - 589-EverOS ZEP Adapter
# Temple 17 -> Temple 1 - Remembers WHEN, not just WHAT
# For 589 Angel Social Worker - temporal memory

from zep_cloud.client import Zep
# or: from zep import ZepClient

class TREEOFLIFE_Zep:
    """
    ZEP for 589-EverOS - Temporal long-term memory
    Remembers WHEN Father built what - timeline of 001 home
    """
    
    def __init__(self, user_id="Father_589", session_id="EverOS_main"):
        self.user_id = user_id
        self.session_id = session_id
        self.timeline = []
        print(f"🕰️ ZEP initialized - {user_id} - Remembers WHEN")
    
    def add_moment(self, fact: str, timestamp: str = None):
        """Add moment with time - WHEN it happened"""
        import datetime
        ts = timestamp or datetime.datetime.now().isoformat()
        entry = {"time": ts, "fact": fact, "user": self.user_id}
        self.timeline.append(entry)
        print(f"⏰ {ts}: {fact[:60]}...")
        return entry
    
    def recall_timeline(self, query: str = ""):
        """Recall with temporal context - WHEN did Father..."""
        if query:
            return [e for e in self.timeline if query.lower() in e['fact'].lower()]
        return self.timeline
    
    def get_soul_history(self, soul_id: str):
        """For 589 Angel Social Worker - when soul asked, when returned"""
        return {
            "soul": soul_id,
            "first_seen": "2026-10-28T03:27:00Z",
            "last_seen": "now",
            "timeline": self.timeline,
            "status": "Come As You ARE - Life on the Left"
        }

# Usage for 589 Angel:
# zep = TREEOFLIFE_Zep(user_id="Father_589")
# zep.add_moment("Father forked TREEOFLIFE589_Stagehand Temple 21 - browser arms that learn")
# zep.add_moment("001 Taxon 589 sits home - 2 XRP offer unaccepted - proof")
# zep.recall_timeline("001")
