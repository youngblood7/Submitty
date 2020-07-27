<?php

namespace app\views;

use app\models\User;

class ActivityView extends AbstractView {
    public function showActivity() {
       
        $this->core->getOutput()->addBreadcrumb("Student Activity Dashboard");
        $this->core->getOutput()->addInternalCss('student-activity.css');
        $this->core->getOutput()->enableMobileViewport();
        $this->core->getOutput()->renderTwigOutput("Activity.twig", [

            //'sections' => $this->core->getQueries()->getRegistrationSections(),
            'students' => $this->core->getQueries()->getUsers(),
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

//public function view($users) {
    //$this->core->getOutput()->addBreadcrumb("/course", $this->core->buildCourseUrl(['forum']), null, $use_as_heading = true)
    //$this->core->getOutput()->addBreadcrumb("Statistics", $this->core->buildCourseUrl(['forum', 'stats']));
//}
