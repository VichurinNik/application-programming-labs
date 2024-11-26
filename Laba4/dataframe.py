import cv2
import matplotlib.pyplot as plt
import pandas as pd


def create_dataframe(file_csv: str) -> pd.DataFrame:
	df = pd.read_csv(file_csv)
	df.columns = ['Relative_path','Absolute_path']
	return df


def add_image(df: pd.DataFrame) -> pd.DataFrame:
	heights = []
	widths = []
	depths = []
	for abs_path in df['Absolute_path']:
			img = cv2.imread(abs_path)
			heights.append(img.shape[0])
			widths.append(img.shape[1])
			depths.append(img.shape[2])

	df['Height'] = heights
	df['Width'] = widths
	df['Depths'] = depths
	return df


def image_statistics(df: pd.DataFrame) -> pd.DataFrame:
    stats = df[['Width', 'Height', 'Depths']].describe()
    return stats


def filter_images_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    filtered_df = df[(df['Width'] <= max_width) & (df['Height'] <= max_height)]
    return filtered_df


def add_area_column(df: pd.DataFrame) -> pd.DataFrame:
    df['Area'] = df['Width'] * df['Height']
    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    sorted_df = df.sort_values(by='Area')
    return sorted_df


def plot_column_distribution(column: pd.Series, x_label_title: str) -> None:
    plt.figure(figsize=(10, 6))
    plt.hist(column, bins=30, color='green', edgecolor='black')
    plt.title('Распределение областей изображения')
    plt.xlabel(x_label_title)
    plt.ylabel('Кол-во изображений')
    plt.show()