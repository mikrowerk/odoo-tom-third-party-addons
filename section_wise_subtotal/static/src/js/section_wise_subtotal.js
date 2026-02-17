/** @odoo-module **/
import { SectionAndNoteListRenderer } from "@account/components/section_and_note_fields_backend/section_and_note_fields_backend"
import { patch } from "@web/core/utils/patch";

patch(SectionAndNoteListRenderer.prototype, {
    setup() {
        super.setup();
        this['subtotal_titleField'] = "price_subtotal";
    },

    isSectionOrNote(record = null) {
        if (this.record) {
            if (this.record.data['display_type'] === 'line_section') {
                var sequence = this.record.data.sequence;
                var all_rows = this.list.records;
                var subtotal = 0.0;
                var self_found = false;

                for (var i = 0; i < all_rows.length; i++) {
                    var row = all_rows[i].data;

                    if (row.sequence == sequence) {
                        self_found = true;
                        continue;
                    }
                    if (self_found) {
                        if (row.display_type === 'line_section' && row.sequence != sequence) {
                            break;
                        }
                        if (!['line_section', 'line_note'].includes(row.display_type)) {
                            // FIX 1: price_subtotal sicher lesen — undefined/null absichern
                            const lineSubtotal = (row.price_subtotal !== undefined && row.price_subtotal !== null)
                                ? row.price_subtotal
                                : 0;
                            subtotal += lineSubtotal;
                        }
                    }
                }

                // FIX 2: Nur setzen wenn das Feld tatsächlich im Record existiert
                if ('price_subtotal' in this.record.data) {
                    this.record.data.price_subtotal = subtotal;
                }
            }
        }

        // FIX 3: record-Parameter sicher auflösen — nie undefined weitergeben
        record = record || this.record;
        if (!record || !record.data) {
            return false;
        }
        return ['line_section', 'line_note'].includes(record.data.display_type);
    },

    getCellClass(column, record) {
        // FIX 4: isSectionOrNote absichern bevor column-Checks
        if (!record || !record.data) {
            return super.getCellClass(column, record);
        }
        var classNames = super.getCellClass(column, record);
        if (
            this.isSectionOrNote(record) &&
            column.widget !== "handle" &&
            column.name !== this.titleField &&
            column.name !== this.subtotal_titleField
        ) {
            return `${classNames} o_hidden`;
        }
        if (column.name === 'price_subtotal' && classNames.includes("o_hidden")) {
            classNames = classNames.replace("o_hidden", "").trim();
        }
        return classNames;
    },

    getColumns(record) {
        // FIX 5: Guard gegen undefined record.data
        if (!record || !record.data) {
            return this.columns;
        }
        const columns = this.columns;
        if (this.isSectionOrNote(record)) {
            if (record.data.display_type === 'line_note') {
                return this.getSectionColumns(columns);
            } else {
                return this.getSubtotalSectionColumns(columns);
            }
        }
        return columns;
    },

    getSubtotalSectionColumns(columns) {
        const sectionCols = columns.filter((col) =>
            col.widget === "handle" ||
            (col.type === "field" && col.name === this.subtotal_titleField) ||
            (col.type === "field" && col.name === this.titleField)
        );
        return sectionCols.map((col) => {
            if (col.name === this.titleField) {
                return { ...col, colspan: columns.length - sectionCols.length + 1 };
            }
            return { ...col };
        });
    }
});