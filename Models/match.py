import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def one_hot_encode(value, categories):
    """One-hot encode a single value or list of values."""
    if isinstance(value, list):
        return [1 if cat in value else 0 for cat in categories]
    else:
        return [1 if value == cat else 0 for cat in categories]

def calculate_similarity_cosine(investor, advisor, categories):
    """
    Calculate similarity using cosine similarity with one-hot encoding for attributes.
    """
    weights = {
        'investment_goals': 0.3,
        'risk_tolerance': 0.2,
        'portfolio_size': 0.15,
        'languages': 0.15,
        'meeting_frequency': 0.05,
        'investment_types': 0.1,
        'interested_industries': 0.05
    }
    
    # Create one-hot encoded vectors for each attribute
    vectors = {}
    for attr in categories:
        investor_vec = one_hot_encode(investor[attr], categories[attr])
        advisor_vec = one_hot_encode(advisor[attr], categories[attr])
        vectors[attr] = (investor_vec, advisor_vec)
    
    # Calculate cosine similarity for each attribute
    match_score = 0
    for attr, (inv_vec, adv_vec) in vectors.items():
        # Reshape to 2D arrays for sklearn cosine_similarity
        inv_vec = np.array(inv_vec).reshape(1, -1)
        adv_vec = np.array(adv_vec).reshape(1, -1)
        similarity = cosine_similarity(inv_vec, adv_vec)[0][0]
        match_score += weights[attr] * similarity
    
    return match_score

# Example usage
investor_profile = {
    'investment_goals': ['Retirement planning', 'Wealth preservation'],
    'risk_tolerance': 'Low',
    'portfolio_size': 'Small',
    'languages': ['English'],
    'meeting_frequency': 'Quarterly',
    'investment_types': ['Bonds', 'Mutual funds'],
    'interested_industries': ['Healthcare']
}

advisor_profiles = [
    {
        'investment_goals': ['Retirement planning', 'Wealth preservation'], 
        'risk_tolerance': 'Low',  
        'portfolio_size': 'Small',  
        'languages': ['English'], 
        'meeting_frequency': 'Quarterly',  
        'investment_types': ['Bonds', 'Mutual funds'],  
        'interested_industries': ['Healthcare']  
    },
    {
        'investment_goals': ['Growth', 'Investment management'], 
        'risk_tolerance': 'High',  
        'portfolio_size': 'Medium', 
        'languages': ['Spanish', 'English'], 
        'meeting_frequency': 'Monthly',  
        'investment_types': ['Stocks', 'ETFs'],  
        'interested_industries': ['Technology']  
    },
    {
        'investment_goals': ['Passive income', 'Tax optimization'],  
        'risk_tolerance': 'Medium',  
        'portfolio_size': 'Large',  
        'languages': ['Chinese'],  
        'meeting_frequency': 'Annually', 
        'investment_types': ['Real estate', 'ETFs'],  
        'interested_industries': ['Energy']  
    },
    {
        'investment_goals': ['Financial education', 'Debt management'],  
        'risk_tolerance': 'Medium',  
        'portfolio_size': 'Small',  
        'languages': ['English', 'Spanish'],  
        'meeting_frequency': 'Monthly',  
        'investment_types': ['Stocks', 'Mutual funds'],  
        'interested_industries': ['Healthcare']  
    },
    {
        'investment_goals': ['Estate planning', 'Wealth preservation'],  
        'risk_tolerance': 'Low', 
        'portfolio_size': 'Large', 
        'languages': ['English', 'French'],  
        'meeting_frequency': 'Annually',  
        'investment_types': ['Bonds', 'Real estate'],  
        'interested_industries': ['Real estate'] 
    },
    {
        'investment_goals': ['Investment management', 'Tax optimization'],  
        'risk_tolerance': 'High', 
        'portfolio_size': 'Medium',  
        'languages': ['English', 'Mandarin'],  
        'meeting_frequency': 'Monthly',  
        'investment_types': ['ETFs', 'Cryptocurrencies'],  
        'interested_industries': ['Technology'] 
    }
]


# Define all possible categories for one-hot encoding
categories = {
    'investment_goals': ['Retirement planning', 'Wealth preservation', 'Education funding', 'Tax optimization'],
    'risk_tolerance': ['Low', 'Medium', 'High'],
    'portfolio_size': ['Small', 'Medium', 'Large'],
    'languages': ['English', 'Spanish', 'French', 'Mandarin'],
    'meeting_frequency': ['Weekly', 'Monthly', 'Quarterly', 'Annually'],
    'investment_types': ['Bonds', 'Stocks', 'Mutual funds', 'Real estate'],
    'interested_industries': ['Healthcare', 'Technology', 'Finance', 'Energy', 'Consumer goods']
}

# Compute scores
scores = [calculate_similarity_cosine(investor_profile, advisor, categories) for advisor in advisor_profiles]
ranked_advisors = sorted(zip(scores, advisor_profiles), key=lambda x: x[0], reverse=True)

# Display results of for sample data
for score, profile in ranked_advisors:
    print(f"Score: {score:.2f}, Profile: {profile}")
