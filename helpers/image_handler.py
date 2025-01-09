from visual_comparison.utils import ImageComparisonUtil


class Image:
    expected_image: ImageComparisonUtil
    actual_image: ImageComparisonUtil

    def __init__(self):
        pass

    def compare_images(self, expected: str, actual: str, result: str, factor: float = 0.99 ):
        expected_image = ImageComparisonUtil.read_image(expected)
        actual_image = ImageComparisonUtil.read_image(actual)
        similarity_index = ImageComparisonUtil.compare_images(expected_image, actual_image, result)
        print(similarity_index)
        return similarity_index > factor
