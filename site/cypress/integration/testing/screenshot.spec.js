describe('screen shot', () => {
    it('test', () => {
        cy.visit('http://localhost');
        cy.screenshot();
    });
});
