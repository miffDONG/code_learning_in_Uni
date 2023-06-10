using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using Debug = UnityEngine.Debug;

public class Astronaut : MonoBehaviour
{
    private AstronautItem myAstronaut;
    private int health;
    private int moveSpeed; // 0: Stop, !0: Move
    private bool isAttacking;
    private bool isStop;
    private bool isStunned = false;
    private Animator astronautAnim;

    [SerializeField]
    private LayerMask layermask;
    [SerializeField]
    private LayerMask astroLayerMask;
    [SerializeField]
    private AstronautSO astronautSO;
    [SerializeField]
    private int characterIndex;

    public Animator GetAstronautAnim
    {
        get { return astronautAnim; }
    }

    void Start()
    {
        astronautAnim = this.GetComponent<Animator>();
        myAstronaut = astronautSO.astronautItems[characterIndex];
        
        if (myAstronaut != null)
        {
            health = myAstronaut.health;
            moveSpeed = myAstronaut.moveSpeed;
        }
    }

    void Update()
    {
        RaycastHit2D hit = Physics2D.Raycast(transform.position, Vector3.right, myAstronaut.attackRange, layermask);

        if (isStunned == true) {
            // Got Stun
            Stop();
        }
        else if (hit.collider != null)
        {
            Stop();
            Attack();
        }
        else if(isStop == true || transform.position.x >= myAstronaut.maxDistance)
        {
            astronautAnim.SetBool("isFight", false);
            Stop();
        }
        else {
            Move();
        }

        /* moveSpeed = 0: Stop, !0: Move */
        transform.Translate(Vector3.right * moveSpeed * Time.deltaTime);
    }

    private void OnTriggerStay2D(Collider2D collision)
    {
        if (collision.CompareTag("Astronaut") && this.transform.position.x < collision.transform.position.x)
        {
            isStop = true;
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        isStop = false;
    }

    // public void AllocateItem(AstronautItem item) {
    // myAstronaut = item;
    // }

    private void Attack()
    {
        if (!isAttacking)
        {
            isAttacking = true;
            astronautAnim.SetBool("isFight", true);
            StartCoroutine("CreateBullet");
        }
    }

    private IEnumerator CreateBullet()
    {
        yield return new WaitForSeconds(myAstronaut.attackSpeed);

        GameObject bullet;
        for (int i=0; i<myAstronaut.attackSpeed; i++) {
            bullet = myAstronaut.BulletPrefab;
            Instantiate(bullet, transform.position, transform.rotation);
        }

        
        // Wait for a short duration before allowing another attack
        isAttacking = false;
    }

    private void Move()
    {
        astronautAnim.SetBool("isWalk", true);
        astronautAnim.SetBool("isFight", false);
        moveSpeed = myAstronaut.moveSpeed;
    }

    private void Stop()
    {
        astronautAnim.SetBool("isWalk", false);
        moveSpeed = 0;
    }

    public void Stun(float stunTime)
    {
        isStunned = true;
        offStun(stunTime);

    }
    private void offStun(float stunTime)
    {
        while (stunTime > 0) {
            stunTime -= Time.deltaTime;
        }
        isStunned = false;
    }

    private void Die()
    {
        Destroy(gameObject);
    }

    IEnumerator DieAnimation()
    {
        astronautAnim.SetBool("isVanish", true);
        yield return new WaitForSeconds(3.0f);
    }

    public void TakeDamage(int damage)
    {
        health -= damage;
        if (astronautAnim.GetBool("isFight") == false && moveSpeed == 0) 
        {   
            astronautAnim.SetBool("isHit", true);
            hitAnimOff(astronautAnim);
        }
        
        if (health <= 0)
        {
            StartCoroutine(DieAnimation());
            Die();
        }   
    }

    public void hitAnimOff(Animator astronautAnim) {
        float sleepTime = 2;
        while (sleepTime > 0) {
            sleepTime -= Time.deltaTime;
        }
        astronautAnim.SetBool("isHit", false);
    }
}
