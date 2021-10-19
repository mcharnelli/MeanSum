from meansum.data_loaders.summ_dataset_factory import SummDatasetFactory
import logging 

from meansum.data_loaders.summ_dataset_factory import SummDatasetFactory
from meansum.project_settings import  HParams
from meansum.utils import save_file, create_argparse_and_update_hp
import argparse

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
 
    parser = argparse.ArgumentParser()
    

    parser.add_argument("--dataset", default=None, required=True, help="yelp,amazon")

    opt = parser.parse_args()



  

    ds = SummDatasetFactory.get(opt.dataset)
    ds.save_processed_splits()
    # ds.print_original_data_stats()
    # ds.print_filtered_data_stats()

    # Variable batch size and n_docs
    # test_dl = ds.get_data_loader(split='test', n_docs_min=4, n_docs_max=16, sample_reviews=True,
    #                              batch_size=1, shuffle=False)
    # test_dl = ds.get_data_loader(split='test', n_docs=8, sample_reviews=False,
    #                              batch_size=1, shuffle=False)
    # for texts, ratings, metadata in test_dl:
    #     x, lengths, labels = ds.prepare_batch(texts, ratings)
    #     pdb.set_trace()
