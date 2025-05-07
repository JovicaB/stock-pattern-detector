## Stock Pattern Detector

Stock Pattern Detector is a machine learning model designed to predict the likelihood of significant price changes based on volume patterns recognized several days before the price movement. The system focuses on analyzing 50-100 companies from a selected sector, where heterogeneity is minimized due to the sector's more uniform business models, allowing for better prediction accuracy.

### Key Features:

- Detects patterns in stock volume that precede significant price changes.
- Predicts the likelihood of a price movement several days in advance.
- Trains on data from 50-100 companies to identify common volume patterns.
- Focuses on the most recent 6 months of data to minimize the influence of long-term historical events.
- The sector with higher homogeneity is chosen to improve model performance and reduce the complexity of diverse industry influences.

### How it Works:

- The model uses stock volume data as the primary feature.
- It identifies recurring patterns in volume activity that typically precede significant price movements.
- The model is trained on historical volume data and predicts whether a stock is likely to experience a significant price change in the coming days.
