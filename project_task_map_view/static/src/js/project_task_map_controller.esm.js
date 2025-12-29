/** @odoo-module */

import {
    Component,
    onMounted,
    onWillStart,
    onWillUpdateProps,
    useState,
} from "@odoo/owl";
import {Layout} from "@web/search/layout";
import {SearchBar} from "@web/search/search_bar/search_bar";
import {useService} from "@web/core/utils/hooks";

export class ProjectTaskMapController extends Component {
    setup() {
        this.orm = useService("orm");
        this.rpc = useService("rpc");
        this.model = useState(
            new this.props.Model(
                this.orm,
                this.rpc,
                this.props.resModel,
                this.env.searchModel,
                this.props.fields,
                this.props.archInfo,
                this.props.domain
            )
        );
        onMounted(async () => {
            await this.model.load();
        });

        onMounted(async () => {
            await this.model.load();
        });

        onWillStart(async () => {
            await this.model.load();
        });

        onWillUpdateProps(async () => {
            await this.model.load();
        });
    }
}

ProjectTaskMapController.components = {Layout, SearchBar};
ProjectTaskMapController.template = "project_task_map_view.View";
