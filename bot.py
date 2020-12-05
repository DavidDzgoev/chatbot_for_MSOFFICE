import message_templates as messages
import lists_of_choices
from botbuilder.dialogs.dialog_reason import DialogReason
from botbuilder.core import ActivityHandler, TurnContext, ConversationState, MessageFactory
from botbuilder.dialogs import DialogSet, WaterfallDialog, WaterfallStepContext
from botbuilder.dialogs.prompts import ChoicePrompt, PromptOptions


class MyBot(ActivityHandler):
    def __init__(self, conversation: ConversationState):
        self.con_state = conversation
        self.state_prop = self.con_state.create_property("dialog_set")
        self.dialog_set = DialogSet(self.state_prop)
        self.dialog_set.add(ChoicePrompt(ChoicePrompt.__name__))
        self.dialog_set.add(
            WaterfallDialog("main_dialog", [self.display_start_choice_list, self.read_start_result]))

    #   Стартовый блок
    #   Выбор
    @staticmethod
    async def display_start_choice_list(waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt(
            ChoicePrompt.__name__,
            PromptOptions(prompt=MessageFactory.text(messages.START), choices=lists_of_choices.START))


    #   Ответ
    async def read_start_result(self, waterfall_step: WaterfallStepContext):
        chat = await self.dialog_set.find('main_dialog')
        start_choice_option = waterfall_step.result.value

        if start_choice_option == '1' or start_choice_option == 'Как работать с Puma':
            chat.add_step(self.read_puma)
            return await chat.run_step(waterfall_step, len(chat._steps) - 1, DialogReason.BeginCalled, None)

        elif start_choice_option == '2' or start_choice_option == 'Результат':
            chat.add_step(self.display_company_choice_list)
            chat.add_step(self.read_finance_result)
            return await chat.run_step(waterfall_step, len(chat._steps) - 2, DialogReason.BeginCalled, None)

        elif start_choice_option == '3' or start_choice_option == 'График закрытия':
            chat.add_step(self.display_company_choice_list)
            chat.add_step(self.read_close)
            return await chat.run_step(waterfall_step, len(chat._steps) - 2, DialogReason.BeginCalled, None)

        elif start_choice_option == '4' or start_choice_option == 'Forex rate':
            chat.add_step(self.display_forex_choice_list)
            chat.add_step(self.read_forex)
            return await chat.run_step(waterfall_step, len(chat._steps) - 2, DialogReason.BeginCalled, None)

        elif start_choice_option == '5' or start_choice_option == 'Процедуры':
            chat.add_step(self.display_company_choice_list)
            chat.add_step(self.read_procedures)
            return await chat.run_step(waterfall_step, len(chat._steps) - 2, DialogReason.BeginCalled, None)

        elif start_choice_option == '6' or start_choice_option == 'Cost Control Team':
            chat.add_step(self.read_cost_control)
            return await chat.run_step(waterfall_step, len(chat._steps) - 1, DialogReason.BeginCalled, None)

        elif start_choice_option == '7' or start_choice_option == 'Контакты Давида':
            chat.add_step(self.read_david)
            return await chat.run_step(waterfall_step, len(chat._steps) - 1, DialogReason.BeginCalled, None)

        return await waterfall_step.end_dialog()

    #   Выбор компании
    @staticmethod
    async def display_company_choice_list(waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt(
            ChoicePrompt.__name__,
            PromptOptions(prompt=MessageFactory.text(messages.COMPANIES), choices=lists_of_choices.COMPANIES))

    #   Puma
    #   Овет бота
    @staticmethod
    async def read_puma(waterfall_step: WaterfallStepContext):
        await waterfall_step._turn_context.send_activity(MessageFactory.text(messages.PUMA))
        return await waterfall_step.end_dialog()

    #   Финсовый результат
    #   Перед ответом бота запускается выбор компании
    #   Ответ бота
    @staticmethod
    async def read_finance_result(waterfall_step: WaterfallStepContext):
        company_choice_option = waterfall_step.result.value

        if company_choice_option == 'Renault':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.RESULT_RENAULT))

        elif company_choice_option == 'Nissan':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.RESULT_NISSAN))

        elif company_choice_option == 'АвтоВАЗ':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.RESULT_LADA))

        return await waterfall_step.end_dialog()

    #   График закрытия
    #   Перед ответом бота запускается выбор компании
    #   Ответ бота
    @staticmethod
    async def read_close(waterfall_step: WaterfallStepContext):
        company_choice_option = waterfall_step.result.value

        if company_choice_option == 'Renault':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.CLOSE_RENAULT))

        elif company_choice_option == 'Nissan':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.CLOSE_NISSAN))

        elif company_choice_option == 'АвтоВАЗ':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.CLOSE_LADA))

        return await waterfall_step.end_dialog()

    #   Forex Rate
    #   Выбор интересующего курса
    @staticmethod
    async def display_forex_choice_list(waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt(
            ChoicePrompt.__name__,
            PromptOptions(prompt=MessageFactory.text(messages.FOREX_CHOICE), choices=lists_of_choices.FOREX_RATE))

    #   Ответ бота
    @staticmethod
    async def read_forex(waterfall_step: WaterfallStepContext):
        company_choice_option = waterfall_step.result.value

        if company_choice_option == 'Текущий':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.FOREX_CURRENT))

        elif company_choice_option == 'Прогнозируемый':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.FOREX_PREDICT))

        return await waterfall_step.end_dialog()

    #   Процедуры
    #   Перед ответом бота запускается выбор компании
    #   Ответ бота
    @staticmethod
    async def read_procedures(waterfall_step: WaterfallStepContext):
        company_choice_option = waterfall_step.result.value

        if company_choice_option == 'Renault':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.PROCEDURES_RENAULT))

        elif company_choice_option == 'Nissan':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.PROCEDURES_NISSAN))

        elif company_choice_option == 'АвтоВАЗ':
            await waterfall_step._turn_context.send_activity(
                MessageFactory.text(messages.PROCEDURES_LADA))

        return await waterfall_step.end_dialog()

    #   Cost Control
    #   Овет бота
    @staticmethod
    async def read_cost_control(waterfall_step: WaterfallStepContext):
        await waterfall_step._turn_context.send_activity(MessageFactory.text(messages.COST_CONTROL))
        return await waterfall_step.end_dialog()

    #   Контакты Давида
    #   Овет бота
    @staticmethod
    async def read_david(waterfall_step: WaterfallStepContext):
        await waterfall_step._turn_context.send_activity(MessageFactory.text(messages.DAVID))
        return await waterfall_step.end_dialog()

    async def on_turn(self, turn_context: TurnContext):
        dialog_context = await self.dialog_set.create_context(turn_context)

        if (dialog_context.active_dialog is not None):
            await dialog_context.continue_dialog()
        else:
            await dialog_context.begin_dialog("main_dialog")

        await self.con_state.save_changes(turn_context)
