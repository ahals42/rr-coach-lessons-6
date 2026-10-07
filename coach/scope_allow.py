"""In-scope topic patterns. A match skips the scope classifier; decline patterns still run first."""

import re

ALLOW_PATTERNS = [re.compile(p) for p in [
    r'(?i)\bself[- ]?reg\b',
    '(?i)\\bplann\\w*',
    '(?i)\\bin the way\\b',
    "(?i)\\b(don'?t|do not|dont)\\s+want to\\b",
    '(?i)\\bkeep\\w*\\s+(moving|going|active)\\b',
    '(?i)\\b(physical|physically)\\s+(activity|activities|active|fitness)\\b',
    '(?i)\\b(exercise|exercises|exercising|workouts?)\\b',
    '(?i)\\b(get|be|stay|getting|being|staying)\\s+(more\\s+)?active\\b',
    '(?i)\\bhow (much|many)\\s+(exercise|activity|minutes|physical activity)\\b',
    '(?i)\\b(150 minutes|two and a half hours|2\\.5 hours)\\b',
    '(?i)\\b(guidelines?|recommendations?)\\b.{0,30}\\b(activity|exercise|moving|movement|active)\\b',
    '(?i)\\bmovement\\b',
    '(?i)\\bmove often\\b',
    '(?i)\\b(sitting|sedentary|sit all day|too much sitting)\\b',
    '(?i)\\b(light|moderate|vigorous|brisk|easy|intense)\\s+(activity|activities|intensity|exercise|walking|effort|pace)\\b',
    '(?i)\\b(strength|strengthening|muscles?|bone[- ]strengthening|balance|falls?|falling|flexibility|stretch(ing)?)\\b',
    '(?i)\\b(walk|walks|walking|cycle|cycling|biking|swim|swimming|gardening|dance|dancing|yoga|tai chi|pickleball|golf|hiking)\\b',
    '(?i)\\b(mood|moods|anxiety|anxious|depression|depressed|stress|stressed|worry|worried|nervous|frustrat\\w*|discouraged|overwhelm\\w*|irritable)\\b',
    '(?i)\\b(brain|memory|attention|concentration|dementia|cognitive|cognition|mental health|health|healthy aging)\\b',
    '(?i)\\b(well-?being|wellbeing|life satisfaction|self-esteem|resilience|energy)\\b',
    '(?i)\\b(retire|retired|retirement|retiree|retirees)\\b',
    '(?i)\\b(lonely|loneliness|isolat\\w*|alone|friends?|social|social support|companions?|community|belong\\w*|connection|group class|walking group)\\b',
    '(?i)\\b(confiden(ce|t)|self-?efficacy|success cycle|small wins?)\\b',
    '(?i)\\b(enjoy|enjoys|enjoyed|enjoyment|enjoyable|fun)\\b',
    '(?i)\\b(Jennifer|Susan|Paul)\\b',
    '(?i)\\b(M-PAC|reflective process|regulatory process|intention-behaviou?r gap|reactive regulation|affective judgements?|perceived (capability|opportunit(y|ies))|instrumental attitude|METs?)\\b',
    '(?i)\\b(goals?|goal[- ]?setting|goal[- ]?choice|flexible goals?|enjoyable goals?|behavio(u)?ral goals?|realistic goals?|starting goal|effective goals?)\\b',
    '(?i)\\b(choos\\w*|pick\\w*|set\\w*|chang\\w*|revis\\w*|rethink\\w*|adjust\\w*|updat\\w*)\\s+(a\\s+|my\\s+|your\\s+|the\\s+|new\\s+)?(starting\\s+)?goals?\\b',
    '(?i)\\bmake (goals?|a plan) work\\b',
    '(?i)\\b(action plan\\w*|coping plan\\w*|back-?up plan\\w*|plan (for|ahead) (enjoyment|enjoying|busy|bad days?|rainy|when)\\w*|planning ahead|make a plan)\\b',
    "(?i)\\bwhat (do|should) i do (if|when) (i )?(miss|skip|can'?t|cannot|forget|get sick|it rains|am busy)\\b",
    '(?i)\\b(stay|stays|staying|keep|keeping|get|getting|back|on)\\s+(on\\s+)?track\\b',
    '(?i)\\b(self[- ]?monitor\\w*|social monitoring|monitor\\w*|track\\w*|log(ging|ged|s)?|journal\\w*|diary|pedometer|step counters?|steps?|fitness trackers?|activity trackers?|wearables?|fitbit|apple watch|checklist|fridge calendar|pathverse|thermostat|garden club|check[- ]in)\\b',
    '(?i)\\b(self[- ]?(regulat\\w*|control|management|discipline)|regulat\\w*)\\b',
    '(?i)\\b(distract\\w*|focus(ed|ing)? (on|during)|mind (wanders?|wandering)|thinking about (something|other things)|zone out|tune out|attention deployment)\\b',
    '(?i)\\b(barriers?|obstacles?|setbacks?|missed days?|missing (a |my |the )?(day|walk|session)|life gets in the way|get in the way|slip(s|ped)? up|intention)\\b',
    "(?i)\\b(motivat\\w*|low motivation|don'?t feel like it|do not feel like it|feel(ing)? like (quitting|giving up|skipping|stopping)|can'?t be bothered|cannot be bothered|not in the mood|on low days)\\b",
    '(?i)\\b(emotion|emotions|emotional|feelings?|mood)\\b',
    '(?i)\\b(emotion regulation|emotional regulation|reframe\\w*|reframing|traffic light|red,? amber,? (and )?green|mindful\\w*|breath\\w*|self[- ]talk|calm\\w* (myself|down)|coping (with|tools?|strategies)|tools for (emotions|feelings))\\b',
    '(?i)\\bvalues?\\b.{0,30}\\b(goal|goals|choos\\w*|pick\\w*|setting)\\b',
    '(?i)\\b(quit\\w*|give up|giving up|keep (at|going|it up|pushing)|stick with|sticking with|stick to|sticking to|push myself|pushing myself|keep myself going)\\b',
    '(?i)\\b(no energy|low energy|bad (day|week)|tough (day|week)|hard days?)\\b',
    '(?i)\\bhow do i stick with it\\b',
]]


def is_allowed(text: str) -> bool:
    return any(p.search(text or '') for p in ALLOW_PATTERNS)


RETRIEVAL_EXPANSIONS = [
    (re.compile(r"(?i)\bself[- ]?regulat\w*|\bself[- ]?control\b|\bself[- ]?management\b"),
     "monitoring your own activity and managing feelings during activity (self-monitoring, emotion regulation)"),
]


def expand_for_retrieval(text: str) -> str:
    """Add the lesson wording a term maps to, so retrieval searches the right lessons."""
    extra = [meaning for pattern, meaning in RETRIEVAL_EXPANSIONS if pattern.search(text or "")]
    return " ".join([text] + extra)
