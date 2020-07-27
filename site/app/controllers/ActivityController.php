<?php

namespace app\controllers;

use app\libraries\Core;
use app\libraries\response\MultiResponse;
use app\libraries\response\WebResponse;
use app\libraries\response\JsonResponse;
use app\libraries\response\RedirectResponse;
//use app\models\Notification;
use Symfony\Component\Routing\Annotation\Route;

/**
 * Class ActivityController
 *
 */
class ActivityController extends AbstractController {

    public function __construct(Core $core) {
        parent::__construct($core);
    }

    /**
     * @Route("/courses/{_semester}/{_course}/activity_dashboard")
     * @return MultiResponse
     */
    public function showActivity() {

        return MultiResponse::webOnlyResponse(
            new WebResponse(
                'Activity', // name of your view
                'showActivity'
            )
        );
    }
}

