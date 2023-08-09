import os
from datasets.load import load_from_disk

os.chdir(os.path.join(os.path.dirname(__file__), '..'))


fill50k_dataset = load_from_disk("HighCWu/diffusiondb_2m_first_5k_canny")
fill50k_dataset.push_to_hub("diffusiondb_2m_first_5k_canny")
