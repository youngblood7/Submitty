<?php

namespace app\views;

use app\models\User;

class ActivityView extends AbstractView {
    public function showActivity() {
        $this->core->getOutput()->addBreadcrumb("Student Activity Dashboard");
        $this->core->getOutput()->addInternalCss('student-activity.css');
        $this->core->getOutput()->enableMobileViewport();
        $this->core->getOutput()->renderTwigOutput("Activity.twig", [
            //'course' => $current_course,
            //'show_all' => $show_all,
            //'notifications' => $notifications,
            //'notification_saves' => $notification_saves,
            //'notifications_url' => $this->core->buildCourseUrl(['notifications']),
            //'mark_all_as_seen_url' => $this->core->buildCourseUrl(['notifications', 'seen']),
            //'notification_settings_url' => $this->core->buildCourseUrl(['notifications', 'settings'])
        ]);
    }
}
