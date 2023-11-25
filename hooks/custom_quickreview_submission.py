import nuke
import sgtk

HookClass = sgtk.get_hook_baseclass()

class CustomQuickReviewSubmission(HookClass):

    def execute(self, **kwargs):
        """
        Main hook entry point
        :returns: None
        """

        # Adding logging
        self.parent.log_info("CustomQuickReviewSubmission hook executed.")

        if self._is_aces_colorspace():
            self.parent.log_info("Detected ACES 1.2 colorspace. Setting QuickTime colorspace to 'Output - sRGB'.")
            quicktime_settings = {
                "colorspace": "Output - sRGB"
                # other settings as needed
            }
        else:
            self.parent.log_info("Default colorspace detected. Using standard QuickTime settings.")
            quicktime_settings = {
                # default settings
            }

        # Apply the settings to the QuickReview process
        self.parent.engine.create_quicktime(quicktime_settings)

    def _is_aces_colorspace(self):
        """
        Determines if Nuke is currently using ACES 1.2 colorspace
        :return: True if in ACES 1.2 colorspace, False otherwise
        """
        aces_detected = "aces_1.2" in nuke.root().knob("OCIO_config").value().lower()
        # Logging the result of colorspace check
        self.parent.log_info(f"ACES 1.2 colorspace detected: {aces_detected}")
        return aces_detected
